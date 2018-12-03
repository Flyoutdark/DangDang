from django.core.paginator import Paginator
from robot_app.models import Creditlost1


class main_pages():
    def ConditionQuery(self,type="北京"):
        if type in ['北京', '上海', '深圳', '广州']:
            data = Paginator(object_list=Creditlost1.objects.filter(areaname='上海').order_by('publishdate'), per_page=50)
            return data
        else:
            self.data = Paginator(object_list=Creditlost1.objects.filter(areaname='北京').order_by('publishdate'), per_page=30)
            return self.data

    # 数据展示
    def InformationBase(self,city='北京', type="AI"):
        self.data = Paginator(object_list=Creditlost1.objects.filter(areaname=city).order_by('publishdate'), per_page=30)
        return self.data


def Left_Information(request):
    pass
