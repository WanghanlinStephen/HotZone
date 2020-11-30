from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from visit.models import *
from virus.models import *
from patient.models import *
import numpy as np
from sklearn.cluster import DBSCAN
import math

# Create your views here.
def index(request):
    """

    :param request:
    :return:
    """
    return render(request, 'clutser/index.html')


def clusterInfo(request):
    """
    Upload image
    :param request:
    :param aid:
    :return:
    """
    defaultDistance=200
    defacultTime=3
    defaultNumber=2
    mylist = []
    distance = request.POST['distance']
    time= request.POST['time']
    number = request.POST['number']

    if distance=='':
        distance=defaultDistance
    if time=='':
        time=defacultTime
    if number=='':
        number=defaultNumber

    distance =int(distance)
    time= int(time)
    number= int(number)

    patientVisits=PatientVisit.objects.all()
    for patientVisit in patientVisits:
        patientInfo=patientVisit.patient
        visitLocationInfo=patientVisit.visitlocation_set.all()
        for visitLocationItem in visitLocationInfo:
            item=[]
            visitInfo=visitLocationItem.visit
            locationInfo=visitLocationItem.location
            x=str(locationInfo.x)
            y=str(locationInfo.y)
            Day=visitLocationItem.date_from.strftime("%j")
            CaseNo=patientInfo.patientcase_set.get().case.case_number
            # print("Date From :"+str(visitLocationItem.date_from))
            # print("Date To :"+str(visitLocationItem.date_to))
            # formatedDate = visitLocationItem.date_from.strftime("%j")
            # print("X :"+str(locationInfo.x))
            # print("Y :"+str(locationInfo.y))
            # print("Case Number :"+str(patientInfo.patientcase_set.get().case.case_number))
            item.append(x)
            item.append(y)
            item.append(Day)
            item.append(CaseNo)
            mylist.append(item)
            print(mylist)
    npArray=np.array(mylist)
    print(npArray.shape)
    result = cluster(npArray,distance,time,number)
    context = {
        "result": result,
        "distance": distance,
        "time": time,
        "number": number
    }
    return render(request, 'clutser/index.html', context)



def custom_metric(q, p, space_eps, time_eps):
    dist = 0
    for i in range(2):
        dist += (q[i] - p[i])**2
    spatial_dist = math.sqrt(dist)

    time_dist = math.sqrt((q[2]-p[2])**2)

    if time_dist/time_eps <= 1 and spatial_dist/space_eps <= 1 and p[3] != q[3]:
        return 1
    else:
        return 2



def cluster(vector_4d, distance, time, minimum_cluster):

    params = {"space_eps": distance, "time_eps": time}
    db = DBSCAN(eps=1, min_samples=minimum_cluster-1, metric=custom_metric, metric_params=params).fit_predict(vector_4d)

    unique_labels = set(db)
    total_clusters = len(unique_labels) if -1 not in unique_labels else len(unique_labels) -1

    print("Total clusters:", total_clusters)

    total_noise = list(db).count(-1)

    print("Total un-clustered:", total_noise)

    result = ClusterInfo(total_clusters, total_noise)

    for k in unique_labels:
        if k != -1:

            labels_k = db == k
            cluster_k = vector_4d[labels_k]

            print("Cluster", k, " size:", len(cluster_k))
            inner = ClusterInner(k, len(cluster_k))
            for pt in cluster_k:
                print("(x:{}, y:{}, day:{}, caseNo:{})".format(pt[0], pt[1], pt[2], pt[3]))
                inner.add_data("(x:{}, y:{}, day:{}, caseNo:{})".format(pt[0], pt[1], pt[2], pt[3]))
            result.add_cluster(inner)
            print()

    return result


class ClusterInfo(object):
    def __init__(self, total_clusters, total_un_clustered):
        self.total_clusters = total_clusters
        self.total_un_clustered = total_un_clustered
        self.clusters = []

    def add_cluster(self, cluster_data):
        self.clusters.append(cluster_data)


class ClusterInner(object):
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.data = []

    def add_data(self, data):
        self.data.append(data)
