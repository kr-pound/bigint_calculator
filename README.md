# bigint_calculator (Python)
ใช้หลักการบวกตัวเลขจากด้านหลัง

# คำอธิบายฟังก์ชัน
- ฟังก์ชัน add(bigintA, bigintB) จะรับ และคำนวณผลรวมในรูปแบบ String

            bigintA
                    +
            bigintB
          __________
             result
          __________

# หลักการทำงานเบื้องต้น
1. บวกตัวเลขหลักสุดท้าย (รวมหลักทด) แล้วเก็บค่าไว้ใน add_temp
2. เขียน result จากหลังมาหน้าโดยเขียนทีละ 1 หลักต่อการบวก 1 ครั้ง แล้วนำเลขหลักด้านหน้าของ add_temp ตั้งเป็นหลักทด
3. ลบตัวเลขหลักสุดท้ายออกจากตัวตั้ง และตัวบวก
4. ทำซ้ำ 1-3 จนกว่า ตัวตั้ง, ตัวบวก, และหลักทด จะมีค่าเป็น 0
