from rest_framework import viewsets as vs,  generics
from .models import material, recipe
from .serializers import materialSerializer, recipeSerilizer

class MaterialVS(vs.ModelViewSet):
    queryset = material.objects.all()
    serializer_class = materialSerializer

class recipeVS(vs.ModelViewSet):
    queryset = recipe.objects.all()
    serializer_class = recipeSerilizer  

class recipeSearchVS(generics.ListAPIView):
    serializer_class = recipeSerilizer
    def get_queryset(self):
        # req_q = {key : value[0] for key, value in {**self.request.POST, **self.request.GET}.items()}
        req_q = {**self.request.POST, **self.request.GET}
        q = {}
        if 'name' in req_q:    q['name__icontains'] = req_q.get('name')[0]
        if 'desc' in req_q: q['describtion__icontains'] = req_q.get('desc')[0]
        if 'review' in req_q: q['review__icontains'] = req_q.get('review')[0]
        if 'min_enerjy' in req_q :q['enerjy__gte'] = req_q.get('min_enerjy') [0] 
        if 'max_enerjy' in req_q : q['enerjy__lte'] = req_q.get('max_enerjy')[0]
        qs =  recipe.objects.filter(**q)
        if 'materials' in req_q :
            for material in req_q.get('materials'):
                qs = qs.filter(materials__id=material)
        return qs