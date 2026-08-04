# 04 — Requirement Candidates: Laundry Queue & Status Tracking

## 1. How We Turned Evidence into Requirement Candidates

**หลักคิดของทีม (Team Case 03):**
1. เริ่มจาก Evidence ที่มี `E-ID` จากบทสัมภาษณ์นักศึกษา แม่บ้าน และผู้ดูแลหอพัก (อ้างอิงจาก Interview Guide Q-01 ถึง Q-10)
2. เขียน `Need` เป็นปัญหา/เป้าหมายของ Stakeholder ที่ต้องการแก้ไข
3. เขียน `RC` (Requirement Candidate) เป็น Capability หรือฟังก์ชันที่ระบบต้องทำได้
4. ใส่ Status เป็น **Candidate** หรือ **Needs Validation**
5. ระบุ Follow-up ประเด็นที่ยังเป็น Unknown เพื่อไปสอบถามและยืนยันต่อใน Week 05

---

## 2. Requirement Candidate Table

| RC-ID | Requirement Candidate | Stakeholder / Need | Evidence E-ID(s) | Status | Follow-up |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **RC-01** | The system should display real-time/simulated availability status and current queue depth for each washing machine before a user joins the queue. | Student Requester / N-01 | E-01 | Candidate | Verify data source of status updates |
| **RC-02** | The system should send automated notification alerts to the user 5 minutes before cycle completion and when it is their turn in queue. | Student Requester / N-02 | E-02 | Needs Validation | Confirm notification channel & timing |
| **RC-03** | The system should automatically cancel a queue reservation if the user fails to confirm presence within the specified timeout limit (e.g., 5-10 mins). | Student Requester / N-03 | E-03 | Needs Validation | Confirm exact timeout duration with Dorm Officer |
| **RC-04** | The system should provide a dedicated logging interface for maids to mark and track moved leftover clothes to specified basket/shelf locations. | Maid, Dorm Officer / N-04 | E-04 | Candidate | Confirm logging fields and SOP rules |
| **RC-05** | The system should allow users to report out-of-order machines and allow dorm officers to disable booking for affected machines immediately. | Student, Dorm Officer / N-05 | E-05 | Candidate | Confirm authorization roles for status override |
| **RC-06** | The system should mask all personal identifiable information (PII) on public status displays, showing only anonymous queue IDs. | Student Requester / N-06 | E-06 | Candidate | Confirm display format for public UI |

---

## 3. Why These Are Candidates, Not Final Requirements

| RC | เหตุผลที่ยังไม่ final |
| :---: | :--- |
| **RC-01** | ยังไม่ยืนยันว่าสถานะเครื่องจะเชื่อมต่อผ่าน IoT Sensor หรือเป็นรูปแบบ Manual Simulation ในเฟสแรก |
| **RC-02** | ยังไม่ตกลงระยะเวลาแจ้งเตือนที่เหมาะสม (เช่น 5 นาที หรือ 10 นาที) และช่องทางแจ้งเตือนหลัก |
| **RC-03** | ยังไม่ได้ข้อสรุปเรื่องตัวเลขเวลา No-show Timeout ที่เป็นธรรมและไม่กระทบต่อผู้ใช้งานช่วง Peak Time |
| **RC-05** | ยังต้องยืนยัน authority ว่านักศึกษาสามารถกดปิดเครื่องเสียได้เลย หรือต้องรอ Dorm Officer/Admin ยืนยันก่อน |

---

## 4. Candidate to Week05 Backlog Handoff

| Week04 RC | Move to Week05? | Reason |
| :---: | :---: | :--- |
| **RC-01** | **Yes** | Evidence ชัดเจนมากว่าเป็น Core Flow ของระบบที่ช่วยลดการเดินฟรี (ตอบ Q-01) |
| **RC-02** | **Yes, revise after validation** | ต้องสรุปตัวเลขเวลาแจ้งเตือนกับนักศึกษาก่อนปรับเป็น Final Requirement (ตอบ Q-04) |
| **RC-03** | **Yes, revise after validation** | ต้องสรุปเวลา Timeout ร่วมกับผู้ดูแลหอพัก (ตอบ Q-03) |
| **RC-04** | **Yes** | เป็น Workflow สำคัญของแม่บ้านในการแก้ปัญหาผ้าค้างเครื่อง (ตอบ Q-05) |
| **RC-05** | **Revise** | ต้องสอบถามสิทธิ์การอนุมัติ (Approval Authority) จากผู้ดูแลหอก่อนเขียน Requirement สรุป (ตอบ Q-06, Q-09) |
| **RC-06** | **Yes** | ตรงตาม Privacy & Responsible AI Plan ที่วางไว้ตั้งแต่ Week 03 (ตอบ Q-07) |

---

## 5. Student Takeaway

งานชิ้นนี้แสดงให้เห็นกระบวนการแปลงข้อความสัมภาษณ์จริง (Evidence) ไปสู่ข้อกำหนดระบบ (Requirement Candidates) โดยมีจุดเน้นคือ:
* **Traceability:** สามารถไล่กลับได้เสมอว่า RC แต่ละข้อมาจาก Evidence (`E-ID`) ไหน ตอบโจทย์ Need (`N-ID`) ใด และเชื่อมโยงกับคำถามสัมภาษณ์ (`Q-ID`) ข้อใด
* **Validation Awareness:** แยกแยะชัดเจนว่า Requirement ข้อใดยังไม่ Final และมีประเด็นใดบ้างที่ต้องนำไปหาคำตอบต่อในสัปดาห์ถัดไป (Week 05)