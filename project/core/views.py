import re
from django.shortcuts import render
from models import *


def editor(request):
    if request.POST:
        name = request.POST.get('name')
        description = request.POST.get('description')
        if not name or not description:
            return render(request, 'editor.html', context={
                    "message": {
                        "tag": "error",
                        "text": "Path has no name or description."
                    }
                }
            )
        pattern = re.compile("poi_\d+$")
        path = Path.objects.create(name=name, description=description)
        for key, value in request.POST.items():
            if pattern.match(key):
                path.save()
                poi_index = key.split('_')[1]
                poi_name = request.POST.get("poi_{index}".format(index=poi_index))
                poi_latitude = request.POST.get("poi_{index}_lat".format(
                    index=poi_index))
                poi_longitude = request.POST.get("poi_{index}_lng".format(
                    index=poi_index))
                if not poi_name or not poi_latitude or not poi_longitude:
                    return render(request, 'editor.html', context={
                            "message": {
                                "tag": "error",
                                "text": "POI {index}'s fields are not filled in.'".format(index=poi_index)
                            }
                        }
                    )
                poi = POI.objects.create(
                    name=poi_name,
                    latitude=poi_latitude,
                    longitude=poi_longitude,
                    path=path)
                poi.save()
        return render(request, 'editor.html', context={
                "message": {
                    "tag": "success",
                    "text": "Path saved successfully."
                }
            }
        )

    return render(request, 'editor.html')
