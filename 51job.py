import happybase
from robot_app.models import  Zhilian


data = Zhilian.objects.filter(pk__lt=6000)
for d in data:
    print(d.city)
# pso1=
# industry=
# netadress=
# numpeople=
# promulgator=
# zw=
# company=
# salary=
# num=
# worktime=
# edu =
# city=
# adress=

# connection = happybase.Connection(host="hadoop33.com")#, port=9090)
# families = {
#     "common":dict(),
#     "uncommon":dict()
# }
# connection.create_table('mydb:foxs',families=families)
# u = str(uuid.uuid4())



# table=connection.table('mydb:foxs')
# table.put(u,{'common:adress':adress,'common:city':city,'common:edu':edu,'common:worktime':worktime,'common:num':num,'common:salary':salary,'common:company':company,'common:zhiwei':zw})
# table.put(u,{'uncommon:psol':pso1,'common:industry':industry,'common:netadress':netadress,'common:numpeople':numpeople,'common:promulgator':promulgator})

# for key,value in table.scan():
#     # print(key.decode('utf-8') ,value)
#     for k ,v in value.items():
#         print(k.decode('utf-8').split(':')[1],v.decode('utf-8'))
#
