from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from jobs.models import Job
from jobs.models import Cities, JobTypes


def joblist(request):
    job_list = Job.objects.order_by('job_type')
    # print(job_list)  # <QuerySet [<Job: Job object (1)>, <Job: Job object (2)>]>
    template = loader.get_template('joblist.html')
    context = {'job_list': job_list}

    for job in job_list:
        job.city_name = Cities[job.job_city][1]
        print(job)
        job.job_type = JobTypes[job.job_type][1]

    return HttpResponse(template.render(context))


def detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.city_name = Cities[job.job_city][1]
    except Job.DoesNotExist:
        raise Http404("Job does not exist")

    return render(request, 'job.html', {'job': job})
