(chadchart) เป็นไลบรารีสำหรับแสดงนโยบายของ “ผู้ว่ากรุงเทพฯ ท่านชัชชาติ สิทธิพันธุ์”
===================================================================================

PyPi: https://pypi.org/project/chadchart/

สวัสดีจ้าาา
สำหรับไลบรารีนี้ลุงได้เขียนขึ้นมาเพื่ออำนวยความสะดวกในการแสดงผล
นโยบายของผู้ว่ากรุงเทพฯ ท่านชัชชาติ สิทธิพันธุ์

-  แสดงนโยบายภาษาไทยและอังกฤษ
-  แสดงนโยบายตามข้อ
-  แสดงหมวดหมู่นโยบาย

วิธีติดตั้ง
~~~~~~~~~~~

เปิด CMD / Terminal

.. code:: python

   pip install chadchart

วิธีใช้งานแพ็คเพจนี้
~~~~~~~~~~~~~~~~~~~~

-  เปิด IDLE/Editor ขึ้นมาแล้วพิมพ์…

.. code:: python

   from chadchart import Policy
   policy = Policy()
   policy.show_all()
   print('All policy:',policy.all)
   print('-----')
   print('Number 1 (dictionary):', policy.number(1))
   print('Number 1 (thai):',policy.number(1)['thai'])
   print('Number 1 (english):',policy.number(1)['english'])
   print('Number 1 (tag):', policy.number(1)['tag'])
   print(policy.all_tag)
   print(policy.all_tag['เรียนดี'])
   policy.show_category()
   policy.category('ปลอดภัยดี')
   policy.credit()
   policy.developer()

พัฒนาโดย: ลุงวิศวกร สอนคำนวณ FB: https://www.facebook.com/UncleEngineer

YouTube: https://www.youtube.com/UncleEngineer
