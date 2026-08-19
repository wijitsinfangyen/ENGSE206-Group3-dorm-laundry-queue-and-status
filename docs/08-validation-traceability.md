# 08 — Validation, Traceability and Baseline Management

> **Case:** Dorm Laundry Queue and Status (Case-03)  
> **Week:** Week 05 Consolidation Studio (Requirement Baseline Review & Readiness Gate)  
> **Status:** Baseline v1.0 Approved & Locked  
> **Target:** ส่งมอบฐานความต้องการสอดคล้อง 100% สำหรับการทำ Requirement Modeling ใน Week 06

---

## 1. Validation Plan

| Validation Activity | Artefact Evaluated | Participants & Roles | Quality Criteria | Verification Evidence Link |
|---|---|---|---|---|
| Artefact Health Check | `docs/01` to `docs/05` | Facilitator, Scribe | Completeness, Recency, Structural Alignment | `../evidence/week-05/baseline-review/health-check.md` |
| Traceability Audit | `docs/04` -> `docs/05` | Traceability Auditor | 100% Must Requirements traceable to E-ID & Stakeholder | Section 3 below & `peer-cross-review.md` |
| Quality & MoSCoW Audit | `docs/05-requirement-backlog.md` | Quality Checker | Verifiable, Unambiguous, Atomic, Rationalized Priority | Section 2 below & `health-check.md` |
| Peer Cross-Review | All Week 05 Artefacts | Cross-Review Team | 5-point Checklist Pass, ID-referenced feedback | `../evidence/week-05/baseline-review/peer-cross-review.md` |
| Baseline Gate Lock | Repo State & Tag | Whole Team | All Gate criteria met, Git tagged `baseline-v1.0` | `project-management/decision-log.md` |

---

## 2. Requirements Quality Checklist

| Quality Dimension | Criteria Description | Evaluation Result | Evidence / Rationale Note |
|---|---|---|---|
| 1. ID Uniqueness & Nomenclature | ทุก Requirement มี ID เฉพาะตามรูปแบบ `[TYPE]-[NO]` ไม่ซ้ำซ้อน | **Pass** | ใช้รหัสชัดเจน: FR-01 ถึง FR-07, NFR-01 ถึง NFR-05, BR-01 ถึง BR-04, ISSUE-DLQS-01 |
| 2. Verifiability (วัด/ทดสอบได้) | มีเกณฑ์ตัวเลขหรือเงื่อนไขที่ตรวจรับได้ ชัดเจน ไม่ใช้คำลอยๆ | **Pass** | กำหนดเงื่อนไขเวลาชัดเจน (Timeout 10 นาที, Latency ≤ 3 วินาที, รองรับผู้ใช้พร้อมกัน 50 คน) |
| 3. Unambiguity (ไม่กำกวม) | อ่านแล้วตีความได้ทางเดียว หลีกเลี่ยงคำลอยๆ | **Pass** | ระบุอำนาจ (Authority) ชัดเจนว่า "ผู้ดูแลหอพัก" เท่านั้นที่มีสิทธิ์กดปิดเครื่องเสีย (BR-03) |
| 4. Atomicity (หนึ่งข้อหนึ่งเรื่อง) | ไม่มัดหลาย workflow ที่แยกกันไว้ในข้อเดียว | **Pass** | แยกการตรวจสอบสถานะ (FR-01) ออกจากการจองคิว (FR-02) และการรายงานเครื่องเสีย (FR-05) |
| 5. Traceability (มีที่มา) | ทุกลูกซอยลากย้อนกลับไปถึง Evidence, Need และ Stakeholder ได้ | **Pass** | มีตาราง Traceability ครบถ้วนย้อนกลับถึงบทสัมภาษณ์ E-01 ถึง E-06 |
| 6. MoSCoW Rationality | Priority มีเหตุผลรองรับ ไม่ใช้ความรู้สึกของทีม | **Pass** | Must ทุกข้อมี Rationale ด้าน Value (ลดการเดินฟรี), Risk (PDPA/กั๊กคิว), Urgency |
| 7. Scope Alignment | ไม่บวมเกินสิ่งที่ Case Card (Case-03) อนุญาต | **Pass** | ปฏิเสธระบบชำระเงินออนไลน์ และการเชื่อมต่อวงจร IoT สั่งเครื่องซักผ้าจริงตาม Out-of-scope (FR-08) |

---

## 3. Traceability Matrix

| Req ID | Requirement Statement (Baseline v1.0) | Priority | Primary Stakeholder | Evidence Trace (E-ID) | Need Trace (N-ID / RC-ID) | Verification / Review Method |
|---|---|---|---|---|---|---|
| FR-01 | ระบบแสดงสถานะความว่างและจำนวนคิวรอจริงของเครื่องซัก/อบผ้า | Must | นักศึกษาหอพัก | E-01 | N-01 / RC-01 | Test case: UI render match database state in real-time |
| FR-02 | ผู้ใช้งานกดเข้าคิวจองเครื่องซักผ้าล่วงหน้าผ่านมือถือได้ | Must | นักศึกษาหอพัก | E-01, E-03 | N-01, N-03 / RC-01 | Queue allocation test (Limit 1 queue/user based on BR-01) |
| FR-03 | ยกเลิกสิทธิ์คิวอัตโนมัติ (No-show Timeout) หากไม่มายืนยันตัวตนใน 10 นาที | Must | นักศึกษา, ผู้ดูแล | E-03 | N-03 / RC-03 | Timer simulation & Auto-skip validation test |
| FR-04 | แจ้งเตือนอัตโนมัติล่วงหน้า 5 นาทีก่อนซักเสร็จ และเมื่อถึงคิว | Must | นักศึกษาหอพัก | E-02 | N-02 / RC-02 | Notification delivery trigger test |
| FR-05 | เปลี่ยนสถานะเครื่องเป็น "ปิดปรับปรุง" (Out of Service) | Must | ผู้ดูแลหอพัก | E-05 | N-05 / RC-05 | RBAC & State transition test (Only Admin can trigger) |
| FR-06 | บันทึกข้อมูลตำแหน่งที่ย้ายผ้าค้างเครื่องไปวางส่วนกลาง | Should | แม่บ้าน, ผู้ดูแล | E-04 | N-04 / RC-04 | Location selection form submit test |
| NFR-01 | ปกปิดข้อมูล PII แสดงเฉพาะรหัสคิวแบบสุ่มบนหน้าจอสาธารณะ | Must | นักศึกษาหอพัก | E-06 | N-06 / RC-06 | UI Privacy review (Check for hidden Name/Room No.) |
| NFR-02 | หน้าจอ Mobile-first เช็กสถานะได้ง่ายใน 3 คลิก | Must | นักศึกษาหอพัก | E-01 | N-01 / RC-01 | Usability & Step count review (≤ 3 clicks) |
| NFR-03 | อัปเดตสถานะคิวและเครื่องล่าช้า (Latency) ไม่เกิน 3 วินาที | Must | นักศึกษา, ผู้ดูแล | E-01 | N-01 / RC-01 | Network response time audit (≤ 3s) |
| NFR-04 | รองรับผู้ใช้งานเข้าพร้อมกันอย่างน้อย 50 Session (Peak Hours) | Should | นักศึกษา, ช่าง IT | E-04 | N/A (Architecture) | Load testing simulation (50 concurrent users) |
| FR-07 | แดชบอร์ดรายงานสถิติการใช้งานและเครื่องชำรุดบ่อย | Could | ผู้ดูแลหอพัก | E-05 | N-05 / RC-05 | Dashboard data query validation |

---

## 4. 3 Traceability Check Form

| Req ID | มาจาก Evidence (E-xx) | ผูกกับ Stakeholder | Need / Candidate (RC) | ลากครบ? | Audit Result & Notes |
|---|---|---|---|---|---|
| FR-01 | E-01 | นักศึกษาหอพัก | RC-01 / N-01 | **[x] ครบ** | ลากย้อนกลับถึง Pain Point เรื่องการเสียเวลาเดินถือตะกร้ามาฟรีได้ชัดเจน |
| FR-03 | E-03 | นักศึกษา, ผู้ดูแล | RC-03 / N-03 | **[x] ครบ** | ลากย้อนกลับถึงความกังวลเรื่องการกั๊กคิวจากระยะไกลและกฎ No-show ได้ |
| NFR-01 | E-06 | นักศึกษาหอพัก | RC-06 / N-06 | **[x] ครบ** | ลากย้อนกลับถึงความต้องการปกปิดข้อมูลส่วนตัวในพื้นที่ส่วนรวมเพื่อความปลอดภัย |

---

## 5. Gap Analysis & Open Questions Log

| Gap / Issue ID | Description of Gap / Open Question | Rationale & Related Evidence | Impact on Requirements | Proposed Action / Week 06 Plan |
|---|---|---|---|---|
| ISSUE-DLQS-03 | ระเบียบปฏิบัติ (SOP) และนโยบายความรับผิดชอบทรัพย์สินเมื่อย้ายผ้าค้างเครื่อง | E-04 (แม่บ้านไม่กล้าย้ายผ้า) | กระทบ Workflow ของ FR-06 (การระบุตำแหน่งวางผ้า) | บันทึกใน `open-questions.md` รอยืนยันนโยบายจากผู้ดูแลหอพักใน Week 06 |
| ISSUE-DLQS-04 | สถาปัตยกรรมข้อมูลสถานะเครื่อง (Sensor จริง หรือ Timer Simulation) | E-01, E-04 (ข้อจำกัด IoT) | กระทบ Implementation ของ FR-01 และ NFR-03 | ยึดการทำ Timer Simulation ไว้เป็น Baseline ก่อน รอยืนยันงบประมาณ IT จากผู้บริหารหอพัก |

---

## 6. Change Request Log

| CR-ID | Date | Requested Change | Reason / Evidence | Impacted Artefacts | Decision | Owner |
|---|---|---|---|---|---|---|
| CR-01 | 2026-08-19 | เพิ่มเกณฑ์ตัวเลขที่วัดผลได้ลงใน NFR และ Business Rules | ผลการประเมิน Quality Audit (เช่น เพิ่ม 10 นาทีสำหรับ No-show, 3 วินาทีสำหรับอัปเดตสถานะ) | `docs/05-requirement-backlog.md` | Approved | Pathomporn (Auditor) |
| CR-02 | 2026-08-19 | ล็อกสถานะ Backlog เป็น Baseline v1.0 | Readiness Gate Check ข้อที่ 5 | `docs/05`, `docs/08`, `decision-log.md` | Approved | Wijitsin (Facilitator) |

---

## 7. Baseline Decision

- **Baseline Name:** `baseline-v1.0`
- **Date:** 19 สิงหาคม 2569
- **Approved/Reviewed by:** ทีม Group 03 (Wijitsin Fangyen - Facilitator, Pathomporn Leejang - Auditor / Scribe)
- **Remaining Open Issues:** `ISSUE-DLQS-03` (Unclaimed laundry policy), `ISSUE-DLQS-04` (Simulation architecture)
- **Sign-off Summary:** ฐานความต้องการ Dorm Laundry Queue and Status ผ่านเกณฑ์ Readiness Gate ครบ 5 ข้อ สมบูรณ์สำหรับการนำไปจัดทำ Requirement Models (User Story, Use Case, Activity Diagram, State Machine) ใน Week 06