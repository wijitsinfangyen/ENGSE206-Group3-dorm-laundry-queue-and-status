# Week 05 Submission

- **Team / Case:** Group 03 — Case 03: Dorm Laundry Queue and Status (ระบบจองคิวและติดตามสถานะเครื่องซักผ้าหอพัก)
- **Repository URL:** `https://github.com/wijitsinfangyen/ENGSE206-Group3-dorm-laundry-queue-and-status`
- **Submission commit:** Example commit message: `submit(w05): prioritize functional and nonfunctional requirements`

## Artefact paths

- `docs/05-requirement-backlog.md`
- `docs/05-prioritization-rationale.md`
- `docs/05-open-questions-and-issues.md`
- `docs/04-evidence-log.md`
- `project-management/team-worklog.md`

## Prioritization Method

ทีมใช้วิธี MoSCoW Method ร่วมกับ Value vs. Effort เพื่อจัดลำดับ Requirement เพราะ Template ของ Week 05 ต้องสรุป Must/Should/Could/Won't ซึ่งวิธีนี้เหมาะกับการคัดแยก Requirement ที่เป็น Core Value (เช่น การดูสถานะเครื่องและการจองคิว) ออกจาก Requirement เสริม หรือฟังก์ชันที่ยังต้องรอความชัดเจนด้านอุปกรณ์และนโยบาย

## What changed from Week 04

- แปลง Requirement Candidates จาก Week 04 ให้เป็น Functional Requirements (FR) ที่สามารถระบุ Acceptance Measure ได้อย่างชัดเจน
- เพิ่ม Non-functional Requirements (NFR) ในด้าน Usability (Mobile-first design), Performance (Real-time sync ดีเลย์ไม่เกิน 3 วินาที), Reliability และ Privacy (การปกปิดข้อมูล PII บนหน้าจอคิวสาธารณะ)
- เพิ่ม Business Rules / Constraints เพื่อควบคุมเงื่อนไขการใช้งาน เช่น จำกัด 1 คนต่อ 1 คิว, กำหนดเวลา No-show Timeout (10 นาที), และการจำกัดสิทธิ์ผู้ดูแลหอพักในการเปลี่ยนสถานะเครื่องชำรุด
- จัดลำดับ Requirement ตามหลักฐาน E-ID และตัดฟังก์ชันที่อยู่นอกขอบเขตในรายวิชานี้ (Won't Have) ออก เช่น การชำระเงินออนไลน์ หรือการเชื่อมต่อระบบสั่งงานวงจรเครื่องซักผ้าจริง (IoT)

## Readiness note for Week 06

Backlog ปัจจุบันมี FR/NFR พร้อม Priority และ Acceptance Measure ที่วัดผลได้แล้ว สามารถนำไปต่อยอดเป็น User Stories, Use Cases, Activity Model และโดยเฉพาะอย่างยิ่ง State Machine Model (สำหรับสถานะการทำงานของเครื่องซักผ้าและสถานะคิว) ใน Week 06 ได้ โดยทีมจะรักษา ID ของ Requirement ไว้เพื่อให้สามารถ Trace กลับมายัง Evidence ในสัปดาห์ก่อนหน้าได้

## Question for instructor

> สำหรับ Requirement ฝั่งแม่บ้าน เรื่องกระบวนการจัดการ "ผ้าค้างเครื่อง" (เช่น การบันทึกตำแหน่งจุดวางผ้าส่วนกลาง) ซึ่งปัจจุบันยังต้องรอนโยบายหอพักและการทำข้อตกลงเรื่องความปลอดภัยของทรัพย์สิน เราควรคงข้อนี้ไว้เป็น Should / Needs Validation ใน Backlog ต่อไป หรือควรย้ายไปไว้ใน Open Issues จนกว่าจะได้ข้อสรุปนโยบายที่ชัดเจนครับ?