from django.shortcuts import render
from django.views.generic import TemplateView
import subprocess
from angelweb.forms import BamForm
import json
import time
from django.http import HttpResponseRedirect, HttpResponseBadRequest
import logging
import requests

LOG = logging.getLogger(__name__)

def bash_view(request):
    template = "home.html"
    form =BamForm()
    context = {'form': form}
    if request.user.is_authenticated:
        current_email=request.user.email
        print(current_email)
        LOG.debug(current_email)
    else:
        current_email = ''
    if request.method == 'POST':
        form = BamForm(request.POST)
        
        if form.is_valid():
            if form.cleaned_data['mutated_allele'] != '':
                variant=form.cleaned_data['mutated_allele']
                variant_list=variant.split('-')
                referenceName=variant_list[0]
                position=variant_list[1]
                referenceBase=variant_list[2]
                alternateBase=variant_list[3]
                r = requests.get('https://aa41372dc8da55.lhr.life/api/g_variants?start={}&alternateBases={}&referenceBases={}&referenceName={}'.format(position, alternateBase, referenceBase, referenceName))
                responsejson=json.loads(r.text)
                variants_list=responsejson["response"]["resultSets"][0]["results"]
                response_list=[]
                for variant in variants_list:
                    response_list.append(variant["variantInternalId"])
                context = {'response': response_list, 'form': form}
        else:
           raise TypeError("can't fill mutated allele if region is specified")        
    
    return render(request, template, context)