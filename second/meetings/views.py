from django.http import Http404
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.core import serializers
import ast
import os
import json

from .models import Meeting

# Create your views here.

def index(request):
	
	latest_meeting_list = Meeting.objects.order_by('id')
	context = {'latest_meeting_list': latest_meeting_list}
	return render(request, 'index.html', context)

def search(request):
	#re = request.GET['x']
	return render(request, 'search.html', context = {})


def get_index_page(request):
	
	latest_meeting_list = Meeting.objects.order_by('id')
	context = {'latest_meeting_list': latest_meeting_list}
	namee = []
	idi = []
	timm = []
	for inn in latest_meeting_list:
		namee.append(inn.name)
		idi.append(inn.id)
		timm.append(inn.tim)
	return HttpResponse(json.dumps({
				'namee':namee,
				'timm':timm,
				'idi':idi
			}), content_type="applications/json", status=200)



def meeting(request, meeting_id):

	try:
		req_meeting = Meeting.objects.get(pk = meeting_id)
		wordDict = ast.literal_eval(req_meeting.words)
		imgs = list(wordDict.keys())
		pth = req_meeting.name
		re = []
		ti = {}
		audio = os.path.join('/static/' + pth + '/audio1.flac')
		if imgs[0] == 'NoImage':
			print('NoImage')
			re = []
			ti = {}
		else:
			#print(imgs)
			for I in imgs:
				file_path = os.path.join('/static/' + pth + '/images/' + I)
				re.append(file_path)
				ti[file_path] = wordDict[I][0]
			#print(re)
	except Meeting.DoesNotExist:
		raise Http404("Meeting does not exist")

	return render(request, 'meeting.html', {'meeting': req_meeting, 'wordDict': wordDict, 'imgs': re, 'I':ti, 'aud':audio})


def temp(request):
	latest_meeting_list = Meeting.objects.order_by('id')
	context = {'latest_meeting_list': latest_meeting_list}
	return render(request, 'temp.html', context)

def get_meeting_images(request):
	print(request.GET)
	req_meeting = Meeting.objects.get(pk = request.GET['id'])
	wordDict = ast.literal_eval(req_meeting.words)
	imgs = list(wordDict.keys())
	return HttpResponse(json.dumps({
				'output': wordDict,
				'imgs': imgs,
				'nam' : req_meeting.name
			}), content_type="applications/json", status=200)

def get_meeting_details(request):
	print(request.GET['x'])

	req_meeting = Meeting.objects.all()
	#data = serializers.serialize('json', req_meeting)
	title = []
	body = []
	idi = []
	print("Get Meeting Details")
	for m in req_meeting:
		title.append(m.name)
		wordDict = ast.literal_eval(m.words)
		imgs = list(wordDict.keys())
		if imgs[0] == "NoImage":
			T = ''
		else:
			T = ''
			for i in range(0, len(imgs)):
				for j in range(1, len(wordDict[imgs[i]])):
					T = T + ' ' + wordDict[imgs[i]][j]
		T = T + ' ' + m.transcript
		body.append(T)
		idi.append(m.id)

	return HttpResponse(json.dumps({
				'titl':title,
				'bod':body,
				'idi':idi
			}), content_type="applications/json", status=200)

def get_search_results(request):
	print(request.GET)
	arr = request.GET['req']
	uparr = [x.strip() for x in arr.split(',')]
	mid = []
	mnames = []
	mtim = []
	final = []
	if len(uparr) != 0 and uparr[0] != '':
		for i in range(0, len(uparr)):
			req_meeting = Meeting.objects.get(pk = uparr[i])
			mid.append(req_meeting.id)
			mnames.append(req_meeting.name)
			mtim.append(req_meeting.tim)
			final.append(req_meeting)
		print("RENDERING")
	#t = loader.get_template('index.html')
	context = {'latest_meeting_list': final}
	return HttpResponse(json.dumps({
				'idi':mid,
				'namee':mnames,
				'timm':mtim
			}), content_type="applications/json", status=200)
	#return HttpResponse(t.render(context, request), content_type='application/xhtml+xml')
	#return render(request, 'searchresult.html', context)