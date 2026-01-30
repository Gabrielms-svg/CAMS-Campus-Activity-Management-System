# app list:

1️⃣ accounts (User \& Role Management)



Core app – everything depends on this



Purpose



Handle authentication \& authorization



Manage Admin / Faculty / Student roles



User status (active, restricted, removed)



Who uses it



Admin (full control)



Faculty \& Students (login/profile)



Models



User (Custom User Model)



username



email



role (ADMIN / FACULTY / STUDENT)



is\_active



StudentProfile



user (OneToOne)



roll\_no



department



semester



FacultyProfile



user (OneToOne)



department



designation



Key Features



Login / Logout



Role-based access



Admin can restrict / remove users



2️⃣ activities (Activity Management)



Heart of the system



Purpose



Create and manage campus activities (sports, arts, tech, etc.)



Who uses it



Admin



Faculty



Models



Activity



title



category (Sports / Arts / Technical)



description



faculty\_incharge



start\_date



end\_date



max\_participants



points



status (Open / Closed / Cancelled)



Key Features



Admin \& Faculty can:



Add / Edit / Delete activities



Students can:



View activities



3️⃣ participation (Student Participation \& Tracking)



Links students ↔ activities



Purpose



Handle student applications and participation status



Who uses it



Students



Faculty



Admin



Models



Participation



student



activity



applied\_on



status (Applied / Approved / Rejected / Cancelled / Completed)



verified\_by (Faculty)



Key Features



Students:



Apply / Cancel participation



Faculty:



Verify participation



Admin:



View all participation records



4️⃣ certificates (Certificate Generation \& Download)



Very good feature for marks



Purpose



Generate \& manage participation certificates



Who uses it



Faculty



Students



Models



Certificate



participation



certificate\_id



issued\_date



file (PDF)



Key Features



Faculty issues certificate after verification



Students download certificates



5️⃣ reports (Points \& Semester Reports)



Important for analytics \& evaluation



Purpose



Activity points calculation



Semester-wise performance reports



Who uses it



Students



Admin



Models



ActivityPoints



student



semester



total\_points



Key Features



Students:



View points \& reports



Admin:



View overall statistics



6️⃣ notifications (Optional but impressive ⭐)



Adds polish to the project



Purpose



Notify users about actions \& updates



Who uses it



All roles



Models



Notification



user



message



created\_at



is\_read



Key Features



Activity approval/rejection alerts



Certificate issued alerts



7️⃣ dashboard (Role-Based Dashboards)



UI-focused app



Purpose



Separate dashboards for Admin / Faculty / Student



Who uses it



All roles



Features



Admin Dashboard:



Total users, activities, participation stats



Faculty Dashboard:



Activities managed, pending verifications



Student Dashboard:



Applied activities, points summary

