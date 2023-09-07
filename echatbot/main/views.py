from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, HttpResponseBadRequest, HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from .models import Conversation, Message
import json
def home(request: HttpRequest):
	return render(request=request, template_name="main/index.html")

@csrf_exempt
def conversations(request : HttpRequest):
	if request.method == "GET":
		convs = Conversation.objects.all()
		convs_objects = []
		for conv in convs:
			convs_objects.append({
				"id": conv.id,
				"created_at" : str(conv.created_at),
				"name": conv.name
			})
		return HttpResponse(content=json.dumps(convs_objects), content_type="application/json")
	elif request.method == "POST":
		body = json.loads(request.body)
		conv = Conversation.objects.create(name=body['name'])
		conv.save()

		conv_json = {
			"id": conv.id,
			"created_at" : str(conv.created_at),
			"name" : conv.name
		}
		return JsonResponse(conv_json)
		
	return HttpResponseBadRequest()
	

@csrf_exempt
def conversation(request : HttpRequest, id : int):
	response = {}
	if request.method == "DELETE":
		try:
			obj = Conversation.objects.get(id=id)
			obj.delete()
			response['status'] = 200
			response['message'] = "deleted conversation " + str(id)
		except:
			response["message"] = "conversation does not exist"
			response['status'] = 404
		return JsonResponse(response)
	elif request.method == 'PUT':
		body = json.loads(request.body)
		obj = Conversation.objects.get(id=id)
		obj.name = body['name'];
		obj.save()
		conv_json = {
			"id": obj.id,
			"created_at" : str(obj.created_at),
			"name" : obj.name
		}
		return JsonResponse(conv_json)
	return HttpResponseBadRequest()

@csrf_exempt
def messages(request : HttpRequest, conv_id: int):
	if request.method == "GET":
		messages = Conversation.objects.get(id=conv_id).message_set.all().order_by("created_at");
		messages_list = []
		for message in messages:
			messages_list.append({
				"content": message.content,
				"id": message.id,
				"conversation_id":message.conversation.id,
				"sender": message.sender,
				"created_at": str(message.created_at)
			})
		return HttpResponse(content=json.dumps(messages_list), content_type="application/json")
	elif request.method == "POST":
		body_obj = json.loads(request.body)
		print(body_obj)
		new_message = Message.objects.create(
			content=body_obj['content'],
			conversation_id=conv_id)
		new_message.save()
		response = {
			"content": new_message.content,
			"id": new_message.id,
			"conversation_id":new_message.conversation.id,
			"sender": new_message.sender,
			"created_at": str(new_message.created_at)
		}
		return JsonResponse(response)
	else:
		HttpResponseBadRequest()