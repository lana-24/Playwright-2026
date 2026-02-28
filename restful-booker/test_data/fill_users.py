from faker import Faker
from datetime import datetime

fake = Faker('id_ID')
valid_users = []
for i in range(2):
    users = (f'{fake.first_name()}{datetime.now().strftime("%m%d_M%S")}',
             f'{fake.last_name()}{datetime.now().strftime("%m%d_%M%S")}',
             f'{fake.email()}{datetime.now().strftime("%m%d_%H%M%S")}',
             f'{fake.bothify(text="08##############")}'
             )
    valid_users.append(users)
    
"""valid_users = [(fake.first_name(),   fake.last_name(),'lanlun12@test.com','1231231238973463'),
               (fake.first_name(),fake.last_name(),'lanlun32@test.com','1231231238976346'),
                  (fake.first_name(),fake.last_name(),'lanlun23@test.com','123123123897463'),
(fake.first_name(), fake.last_name(),'lanlun312@test.com','12312312384637'),
(fake.first_name(), fake.last_name(),'lanlun412@test.com','123123123896347'),
                  (fake.first_name(),fake.last_name(),'lanlun1231@test.com','123123123864397'),
                  (fake.first_name(),fake.last_name(),'lanlun3213@test.com','123123123857474'),
                  (fake.first_name(),fake.last_name(),'lanlun231@test.com','12312312342457'),
                  (fake.first_name(),fake.last_name(),'lanlun1431@test.com','12312312845497'),
                  (fake.first_name(),fake.last_name(),'lanlun131@test.com','12312312457497')
            ]
"""

invalid_users = [('la','lu','lanlun12@','123123'),
                  ('li','lu','lanlun32@','11231'),
                  ('lu','lu','lanlun23@','131233'),
                  ('lo','lu','lanlun312@','1231231'),
                  ('le','l','lanlun412@','12347'),
                  ('ta','lu','lanlun1231@','1264397'),
                  ('ti','ne','lanlun3213@','157474'),
                  ('tu','nd','lanlun231@','122457'),
                  ('te','nh','lanlun13431@','1297'),
                  ('to','ln','lanlun131@','12357497'),
                  ('yu','lu','lanlun122@','125497'),
                  ('yi','nf','lanlun434@','1228497'),
                  ('la','lu','lanlun43@','123887'),
                  ('la','lf','lanlun542@','123297'),
                  ('en','na','lanlun4216','12197'),
                  ('le','lu','lanlun6641','1177897'),
                  ('la','lu','lanlun6325','123197')
            ]

#firstname size under 3
invalid_firstname = [('la','lunr','lanlun12@test.com','1231232313131'),
                  ('li','lunr','lanlun32@test.com','1231231231213'),
                  ('lu','lunq','lanlun23@test.com','123123331231'),
                  ('lo','lunq','lanlun312@test.com','12312312131231'),
                  ('le','ladsa','lanlun412@test.com','123823131296347'),
                  ('ta','lune','lanlun1231@test.com','126439312217'),
                  ('ti','lune','lanlun3213@test.com','157473123124'),
                  ('tu','lund','lanlun231@test.com','122451231217'),
                  ('te','lunh','lanlun13431@test.com','129231132317'),
                  ('to','lung','lanlun131@test.com','123574931317')
            ]

invalid_lastname = [('laf','lu','lanlun12@test.com','12312341241'),
                  ('lin','lr','lanlun32@test.com','12312312313123112'),
                  ('lun','lu','lanlun23@test.com','1231233412412'),
                  ('lon','lg','lanlun312@test.com','123123123112'),
                  ('lefd','la','lanlun412@test.com','123831239634712'),
                  ('tan','lf','lanlun1231@test.com','1264397321312321'),
                  ('tin','lf','lanlun3213@test.com','15747432424123121'),
                  ('tun','ls','lanlun231@test.com','122457341421123123'),
                  ('ten','lu','lanlun13431@test.com','129732131123123'),
                  ('ton','lu','lanlun131@test.com','12357493427123123'),
                  ('yun','lu','lanlun122@test.com','125493123217123')
            ]

invalid_email = [('lda','lunr','lanlun12@','12312341214123'),
                  ('lin','lunr','lanlun32@','1231231234122112'),
                  ('lun','lunq','lanlun23@','123123341241'),
                  ('lon','lunq','lanlun312@','123123141241'),
                  ('lea','lfa','lanlun412@','123896347411123'),
                  ('tan','lune','lanlun1231@','126439741241'),
                  ('tin','lune','lanlun3213@','1574743242412'),
                  ('tun','lund','lanlun231@','122457412124331'),
                  ('ten','lunh','lanlun13431@','1297123123121'),
                  ('ton','lung','lanlun131@','12357497231123'),
                  ('yun','lunv','lanlun122@','125497231123')
            ]

invalid_phone = [('lada','lunr','lanlun12@test.com','123123'),
                  ('lin','lunr','lanlun32@test.com','1231231'),
                  ('lun','lunq','lanlun23@test.com','1231233'),
                  ('lon','lunq','lanlun312@test.com','1231231'),
                  ('led','lasd','lanlun412@test.com','12896347'),
                  ('tan','lune','lanlun1231@test.com','1264397'),
                  ('tin','lune','lanlun3213@test.com','157474'),
                  ('tun','lund','lanlun231@test.com','122457'),
                  ('ten','lunh','lanlun13431@test.com','1297'),
                  ('ton','lung','lanlun131@test.com','12357497'),
                  ('yun','lunv','lanlun122@test.com','125497')
            ]
