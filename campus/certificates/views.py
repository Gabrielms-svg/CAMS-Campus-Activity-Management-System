from django.shortcuts import get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Certificate
from participation.models import Participation
import io
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.units import inch

@login_required
def download_certificate(request, participation_id):
    participation = get_object_or_404(Participation, pk=participation_id, student=request.user)
    
    if participation.status not in ['APPROVED', 'COMPLETED']:
        return HttpResponse("Certificate not available yet.", status=403)

    # Get or create certificate object
    certificate, created = Certificate.objects.get_or_create(participation=participation)
    
    # Create PDF buffer
    buffer = io.BytesIO()
    
    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=landscape(A4))
    width, height = landscape(A4)
    
    # --- Design Elements ---
    
    # 1. Border
    p.setStrokeColor(colors.darkblue)
    p.setLineWidth(5)
    p.rect(0.5*inch, 0.5*inch, width-1*inch, height-1*inch)
    
    # 2. Logo (Moved to Top Center, smaller)
    logo_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'college_logo.png')
    logo_height = 1.5*inch
    logo_y_bottom = height - 2.2*inch
    
    if os.path.exists(logo_path):
        try:
           # Centered Logo
           p.drawImage(logo_path, width/2 - 0.75*inch, logo_y_bottom, width=1.5*inch, height=1.5*inch, mask='auto', preserveAspectRatio=True)
        except Exception as e:
           print(f"Error loading image: {e}")
    
    # 3. Header (College Name) - Moved below logo
    p.setFont("Helvetica-Bold", 30)
    p.setFillColor(colors.darkblue)
    p.drawCentredString(width/2, height - 2.6*inch, "Nirmala College of Engineering")
    
    p.setFont("Helvetica", 16)
    p.setFillColor(colors.black)
    p.drawCentredString(width/2, height - 2.9*inch, "Meloor, Chalakudy")
    
    # 4. Certificate Text
    p.setFont("Helvetica-Bold", 36)
    p.setFillColor(colors.gold)
    p.drawCentredString(width/2, height - 4.0*inch, "CERTIFICATE OF PARTICIPATION")

    p.setFont("Helvetica", 14)
    p.setFillColor(colors.black)
    p.drawCentredString(width/2, height - 4.5*inch, "This is to certify that")
    
    # Student Name
    student_name = participation.student.get_full_name() or participation.student.username
    p.setFont("Times-BoldItalic", 30)
    p.setFillColor(colors.darkblue)
    p.drawCentredString(width/2, height - 5.1*inch, student_name)
    
    p.setFont("Helvetica", 14)
    p.setFillColor(colors.black)
    p.drawCentredString(width/2, height - 5.6*inch, "has successfully participated in the activity")
    
    # Activity Title
    p.setFont("Times-Bold", 24)
    p.drawCentredString(width/2, height - 6.2*inch, participation.activity.title)
    
    # Date and Faculty
    p.setFont("Helvetica", 12)
    p.drawString(1.5*inch, 1.5*inch, f"Date: {participation.activity.start_date.strftime('%Y-%m-%d')}")
    
    faculty_name = participation.activity.faculty_incharge.get_full_name() or participation.activity.faculty_incharge.username
    p.drawString(width - 4*inch, 1.5*inch, f"Faculty in Charge: {faculty_name}")

    # Unique ID
    p.setFont("Helvetica", 8)
    p.drawCentredString(width/2, 0.8*inch, f"Certificate ID: {certificate.certificate_id}")

    p.showPage()
    p.save()

    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="certificate_{participation.id}.pdf"'
    return response
