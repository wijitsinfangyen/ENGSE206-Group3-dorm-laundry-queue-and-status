# Week 04 — AI Conversation Excerpt

## Session Information

| Field | Value |
| --- | --- |
| **Date** | 04/08/2026 |
| **Case** | Dorm-Laundry-Queue-and-Status |
| **AI role** | ผู้ใช้งานเครื่องซักผ้า (นักศึกษาหอพัก), ผู้ดูแลหอพัก (Dorm Admin), ช่างเทคนิค/ผู้ดูแลระบบ IT |
| **Team interviewer(s)** | Interview ENGSE206 Group 3 |
| **Source used** | Interview Transcripts (Resident Student, Dorm Admin, IT/Technician) |

---

## Prompt Used

You are simulating the stakeholder role [ROLE] in case Dorm-Laundry-Queue-and-Status only for a software-requirements interview rehearsal.
Allowed context:
- Case facts: [Specific to role]
- Role goal: [Specific to role]
- Role concerns: [Specific to role]
- Authority boundary: [Medium/High]
Rules:
1. Answer only from this role's viewpoint and authority.
2. If information is absent, say that you do not know or another role owns it.
3. Do not invent policies, statistics, personal data, or confidential information.
4. Do not generate a feature list or reveal everything at once.
5. Give more detail only when the interviewer asks a useful probe.
6. Distinguish simulated fact/rule, personal opinion, assumption, and solution suggestion.
7. Stay internally consistent and allow the interviewer to paraphrase for confirmation.
8. Answer one question at a time.


### Conversation Excerpt A — ผู้ใช้งานเครื่องซักผ้า (นักศึกษาหอพัก)

| Turn | Question / Answer | Why this matters | Link to E-ID |
| :---: | :--- | :--- | :---: |
| **Q1** | เวลาที่คุณจะไปซักผ้าที่ใต้หอพัก ปัญหาที่เจอบ่อยที่สุดคืออะไร  และมีวิธีรับมืออย่างไร? | เปิดให้ stakeholder เล่า Pain Point และพฤติกรรมจริงในการใช้งานเครื่องซักผ้าหอพัก | **E-01** |
| **A1** | เดินถือตะกร้าผ้าลงมาแล้วเครื่องเต็มตลอด ต้องนั่งรอหรือแบกผ้ากลับห้อง และบางครั้งผ้าซักเสร็จแล้วแต่เจ้าของไม่มาเอาออก ทำให้คนอื่นใช้ต่อไม่ได้ ไม่กล้าหยิบผ้าคนอื่นออกเพราะกลัวมีปัญหา | ใช้เป็น evidence เรื่องการไม่มีข้อมูลสถานะแบบ Real-time และปัญหาผ้าค้างเครื่อง | **E-01, E-02** |
| **Q2** | จากที่เราได้พูดคุยกันมาทั้งหมด ทีมงานขออนุญาตสรุปเพื่อทวนความเข้าใจ... ตรงนี้มีจุดไหนที่ทางเราเข้าใจคลาดเคลื่อน หรือมีข้อเสนอแนะ/ข้อควรระวังเพิ่มเติมไหมครับ? | ทวนความเข้าใจและหาความต้องการเชิงลึกเกี่ยวกับการจองคิวและการแจ้งเตือน | **E-02** |
| **A2** | อยากให้มีระบบแจ้งเตือนเมื่อผ้าซักเสร็จ หรือเมื่อถึงคิวซัก และอยากให้มีระยะเวลาผ่อนผัน (Grace Period) เช่น 5-10 นาที ถ้าถึงคิวแล้วไม่มาใส่ผ้าให้ข้ามคิวทันที เพื่อป้องกันการกั๊กคิว | ใช้เป็น evidence เรื่องระบบ Notification และเงื่อนไขการจัดการคิว (Queue Management) | **E-02** |

---

### Conversation Excerpt B — ผู้ดูแลหอพัก (Dorm Admin)

| Turn | Question / Answer | Why this matters | Link to E-ID |
| :---: | :--- | :--- | :---: |
| **Q1** | ปัจจุบันเมื่อเครื่องซักผ้าเสียหรือเหรียญติด ทางหอพักมีขั้นตอนการจัดการอย่างไร และผู้ใช้แจ้งปัญหาผ่านช่องทางไหน? | ค้นหากระบวนการจัดการปัญหาหน้างานและช่องทางการรับแจ้งเรื่องร้องเรียน | **E-03** |
| **A1** | ผู้ใช้มักจะมาเขียนโน้ตแปะไว้ หรือแจ้งไลน์ส่วนตัวผู้ดูแล ทำให้ตกหล่น การประสานงานกับช่างใช้เวลานาน และไม่มีป้ายบอกชัดเจนทำให้คนอื่นมาหยอดเหรียญซ้ำจนเงินกินเหรียญ | ใช้เป็น evidence เรื่องระบบรายงานเครื่องชำรุด (Issue Reporting) และการจัดการสถานะเครื่อง | **E-03** |
| **Q2** | ...ตรงนี้มีจุดไหนที่ทางเราเข้าใจคลาดเคลื่อน หรือมีข้อเสนอแนะ/ข้อควรระวังเพิ่มเติมที่ยังไม่ได้กล่าวถึงในวันนี้อีกไหมครับ? | หาข้อจำกัดและขอบเขตอำนาจหน้าที่ของผู้ดูแลหอพัก | **E-03, E-05** |
| **A2** | ต้องการระบบที่ผู้ดูแลสามารถกดปิดปรับปรุงสถานะเครื่อง (Out of Service) ได้ทันที เพื่อไม่ให้คนกดจองคิวเพิ่ม และอยากเห็นรายงานสรุปเครื่องที่เสียบ่อยเพื่อนำไปแจ้งเจ้าของสัมปทาน | ใช้เป็น evidence เรื่อง Admin Control Dashboard และรายงานสถิติการใช้งาน | **E-03, E-05** |

---

### Conversation Excerpt C — ช่างเทคนิค / ผู้ดูแลระบบ IT

| Turn | Question / Answer | Why this matters | Link to E-ID |
| :---: | :--- | :--- | :---: |
| **Q1** | ในมุมมองของการเชื่อมต่อระบบและการตรวจจับสถานะเครื่องซักผ้า มีข้อจำกัดทางเทคนิคหรือนโยบายด้านความปลอดภัยอย่างไรบ้าง? | ค้นหาข้อจำกัดด้าน Architecture, การรับส่งข้อมูล Real-time และความปลอดภัย | **E-04** |
| **A1** | เครื่องซักผ้าเป็นรุ่นหยอดเหรียญทั่วไป ไม่ใช่ IoT Smart Washer ตั้งแต่แรก การเช็กสถานะจึงต้องพึ่งพาข้อมูลการจับเวลา (Timer Sync) หรือ Sensor ภายนอก และระบบต้องรองรับการเรียกข้อมูลพร้อมกันช่วง Peak Hours (18:00 - 22:00 น.) | ใช้เป็น evidence เรื่อง Non-functional Requirements (Performance & Hardware constraints) | **E-04** |

---

### Team Notes

* **Evidence ที่ใช้ได้ทันที:** `E-01` ถึง `E-05`
* **Unknown สำคัญ:**
  * รูปแบบการตรวจจับสถานะเครื่องซักผ้าที่แน่ชัด (ใช้ระบบสั่งงานผ่านแอป/Sensor หรือใช้การจับเวลาถอยหลังจากการกดใช้จริง)
  * นโยบายการจัดการผ้าที่ค้างอยู่ในเครื่องเกินเวลา (ใครมีสิทธิ์ย้ายผ้า และมีพื้นที่กลางสำหรับวางผ้าค้างหรือไม่)
  * นโยบายการคืนเงินในกรณีระบบขัดข้อง หรือเครื่องกินเหรียญ
* **ข้อควรระวัง:** โครงสร้าง hardware ของเครื่องซักผ้าเดิมยังไม่รองรับ IoT เต็มรูปแบบ ห้ามออกแบบ Feature สั่งเปิด-ปิดเครื่องผ่านแอปโดยตรง (Final System Requirement) จนกว่าจะได้รับนโยบายงบประมาณปรับปรุงอุปกรณ์จากผู้บริหารหอพัก