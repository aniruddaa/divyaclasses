# Custom animated admin panel view
from .models import Enquiry, LectureVideo, Testimonial, Faculty
from django.utils.html import escape

def admin_panel(request):
	return render(request, 'admin_panel.html')

# AJAX endpoint for enquiries table
def admin_enquiries(request):
	rows = []
	for e in Enquiry.objects.order_by('-submitted_at')[:20]:
		rows.append(f"<tr><td>{escape(e.name)}</td><td>{escape(e.email)}</td><td>{escape(e.phone)}</td><td>{escape(e.standard)}</td><td>{escape(e.message)}</td><td>{e.submitted_at.strftime('%Y-%m-%d')}</td></tr>")
	return JsonResponse(''.join(rows), safe=False)

# AJAX endpoint for videos table
def admin_videos(request):
	rows = []
	for v in LectureVideo.objects.order_by('-uploaded_at')[:20]:
		rows.append(f"<tr><td>{escape(v.title)}</td><td>{escape(v.description)}</td><td>{v.uploaded_at.strftime('%Y-%m-%d')}</td></tr>")
	return JsonResponse(''.join(rows), safe=False)
from django.shortcuts import render
# Dedicated enquiry page view
def enquiry_page(request):
	return render(request, 'enquiry.html')
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def ai_chatbot_api(request):
	if request.method == 'POST':
		user_msg = request.POST.get('message', '').lower()
		lang = request.POST.get('lang', 'en')
		import random, re
		motivational_quotes = {
			'en': [
				"Success is the sum of small efforts, repeated day in and day out.",
				"Believe in yourself! You are capable of amazing things.",
				"Hard work beats talent when talent doesn't work hard.",
				"Every day is a new beginning. Take a deep breath and start again.",
				"Dream big, work hard, stay focused, and surround yourself with good people."
			],
			'mr': [
				"यश म्हणजे दररोज केलेल्या छोट्या प्रयत्नांची बेरीज आहे.",
				"स्वतःवर विश्वास ठेवा! तुम्ही अद्भुत गोष्टी करू शकता.",
				"परिश्रम हेच खरे यशाचे गमक आहे.",
				"प्रत्येक दिवस नवीन संधी घेऊन येतो. शांत राहा आणि पुन्हा सुरुवात करा.",
				"मोठी स्वप्ने बघा, मेहनत करा, लक्ष केंद्रित ठेवा आणि चांगल्या लोकांसोबत रहा."
			]
		}
		study_tips = {
			'en': [
				"Make a study schedule and stick to it.",
				"Take regular breaks to improve focus.",
				"Practice with previous years' question papers.",
				"Teach someone else to better understand the topic.",
				"Stay hydrated and get enough sleep before exams."
			],
			'mr': [
				"अभ्यासाचे वेळापत्रक तयार करा आणि त्याचे पालन करा.",
				"एकाग्रता वाढवण्यासाठी नियमित ब्रेक घ्या.",
				"मागील वर्षांचे प्रश्नपत्रिका सोडवा.",
				"इतरांना शिकवा म्हणजे तुम्हालाही समजेल.",
				"परीक्षेपूर्वी पुरेशी झोप आणि पाणी प्या."
			]
		}

		if not user_msg.strip():
			if lang == 'mr':
				return JsonResponse({'success': True, 'reply': "नमस्कार! मी तुमच्या करिअर, अभ्यास किंवा दिव्या क्लासेसबद्दल कशी मदत करू शकते?"})
			else:
				return JsonResponse({'success': True, 'reply': "Hello! How can I help you with your career, studies, or Divya Classes information today?"})

		# Fun and utility features
		if 'motivat' in user_msg or 'inspire' in user_msg or 'quote' in user_msg:
			reply = random.choice(motivational_quotes.get(lang, motivational_quotes['en']))
		elif 'study tip' in user_msg or 'how to study' in user_msg or 'exam tip' in user_msg:
			reply = random.choice(study_tips.get(lang, study_tips['en']))
		elif re.match(r'what is \d+ [\+\-\*/] \d+', user_msg):
			# Simple math help: e.g., "what is 5 + 3"
			try:
				expr = user_msg.split('what is',1)[1].strip()
				result = str(eval(expr))
				if lang == 'mr':
					reply = f"उत्तर: {result}"
				else:
					reply = f"The answer is {result}."
			except Exception:
				if lang == 'mr':
					reply = "माफ करा, मी ते गणना करू शकले नाही. कृपया साधे गणिती उदाहरण विचारा."
				else:
					reply = "Sorry, I couldn't calculate that. Please use simple math expressions like 'what is 5 + 3'."
		# Contextual responses
		elif 'divya' in user_msg and 'class' in user_msg:
			if lang == 'mr':
				reply = "दिव्या क्लासेस ८वी ते १२वी, JEE, NEET, CET साठी मार्गदर्शन करते. आमच्या कोर्सेस किंवा सुविधा विचारू शकता!"
			else:
				reply = "Divya Classes is dedicated to helping students from 8th to 12th, including JEE, NEET, and CET preparation. Ask about our courses or facilities!"
		elif 'location' in user_msg or 'where' in user_msg:
			if lang == 'mr':
				reply = "दिव्या क्लासेस आपल्या शहरात आहे. नेमका पत्ता जाणून घेण्यासाठी enquiry पेज वापरा."
			else:
				reply = "Divya Classes is located in your city. For the exact address, please contact us through the enquiry page."
		elif 'fees' in user_msg or 'fee' in user_msg or 'cost' in user_msg:
			if lang == 'mr':
				reply = "कोर्सनुसार फी वेगवेगळी आहे. कृपया enquiry फॉर्म भरा किंवा कॉल करा."
			else:
				reply = "For detailed fee structure, please fill the enquiry form or call us. Fees vary by course and standard."
		elif 'timing' in user_msg or 'time' in user_msg or 'schedule' in user_msg:
			if lang == 'mr':
				reply = "क्लासचे वेळापत्रक बॅच आणि वर्गानुसार बदलते. कृपया आपला वर्ग सांगा किंवा संपर्क साधा."
			else:
				reply = "Class timings depend on the batch and standard. Please mention your class or contact us for details."
		elif 'admission' in user_msg or 'enroll' in user_msg or 'join' in user_msg:
			if lang == 'mr':
				reply = "प्रवेश सुरू आहेत! enquiry फॉर्म भरा किंवा आमच्या सेंटरला भेट द्या."
			else:
				reply = "Admissions are open! You can enroll by filling the enquiry form or visiting our center."
		elif 'engineering' in user_msg:
			if lang == 'mr':
				reply = "इंजिनिअरिंगसाठी १२वी नंतर JEE किंवा CET ची तयारी करा. फिजिक्स, केमिस्ट्री, मॅथ्सवर लक्ष केंद्रित करा."
			else:
				reply = "Engineering is a great field! You can prepare for JEE or CET exams after 12th. Focus on Physics, Chemistry, and Maths."
		elif 'medical' in user_msg or 'doctor' in user_msg or 'neet' in user_msg:
			if lang == 'mr':
				reply = "मेडिकलसाठी NEET मुख्य परीक्षा आहे. बायोलॉजी, केमिस्ट्री, फिजिक्सवर लक्ष द्या."
			else:
				reply = "For a medical career, NEET is the main entrance exam. Focus on Biology, Chemistry, and Physics."
		elif 'commerce' in user_msg:
			if lang == 'mr':
				reply = "कॉमर्समध्ये CA, CS, बँकिंग, बिझनेससारख्या करिअरच्या संधी आहेत. अकाउंट्स, इकॉनॉमिक्स, बिझनेस स्टडीज शिकवा."
			else:
				reply = "Commerce opens up careers in CA, CS, banking, and business. Subjects include Accountancy, Economics, and Business Studies."
		elif 'science' in user_msg:
			if lang == 'mr':
				reply = "सायन्समध्ये इंजिनिअरिंग, मेडिकल, रिसर्चसारख्या अनेक संधी आहेत. आपल्या आवडीप्रमाणे निवडा."
			else:
				reply = "Science stream offers many options: engineering, medical, research, and more. Choose based on your interest."
		elif 'jee' in user_msg:
			if lang == 'mr':
				reply = "JEE ही इंजिनिअरिंगसाठी आहे. मॅथ्स, फिजिक्स, केमिस्ट्रीचा सराव करा."
			else:
				reply = "JEE is for engineering aspirants. Practice Maths, Physics, and Chemistry regularly."
		elif 'career' in user_msg:
			if lang == 'mr':
				reply = "१०वी आणि १२वी नंतर अनेक करिअर पर्याय आहेत. आपली आवड किंवा विषय सांगा."
			else:
				reply = "There are many career options after 10th and 12th. Tell me your interests or subjects you like."
		elif '8th' in user_msg or '9th' in user_msg or '10th' in user_msg:
			if lang == 'mr':
				reply = "सर्व विषयांची मजबूत पायाभरणी करा. आवडता विषय असल्यास सांगा!"
			else:
				reply = "Focus on building strong basics in all subjects. If you have a favorite subject, let me know!"
		elif '11th' in user_msg or '12th' in user_msg:
			if lang == 'mr':
				reply = "११वी आणि १२वीमध्ये Science, Commerce, Arts पैकी योग्य निवडा. प्रत्येकात उत्तम संधी आहेत."
			else:
				reply = "In 11th and 12th, choose your stream wisely: Science, Commerce, or Arts. Each has great opportunities."
		elif 'thank' in user_msg:
			if lang == 'mr':
				reply = "तुमचे स्वागत आहे! अजून काही प्रश्न असतील तर विचारा."
			else:
				reply = "You're welcome! If you have more questions, just ask."
		elif 'contact' in user_msg or 'phone' in user_msg:
			if lang == 'mr':
				reply = "अधिक माहितीसाठी enquiry पेज वापरा किंवा आमच्या सेंटरला भेट द्या."
			else:
				reply = "You can contact us through the enquiry page or visit our center for more information."
		elif 'subjects' in user_msg:
			if lang == 'mr':
				reply = "आम्ही ८वी-१२वी, JEE, NEET, CET साठी Maths, Science, English इ. शिकवतो."
			else:
				reply = "We offer coaching for Maths, Science, English, and more for 8th-12th, as well as JEE, NEET, and CET."
		elif 'facilities' in user_msg or 'infrastructure' in user_msg:
			if lang == 'mr':
				reply = "आमच्याकडे आधुनिक क्लासरूम, अनुभवी शिक्षक आणि डिजिटल लर्निंग सुविधा आहेत."
			else:
				reply = "We provide modern classrooms, experienced faculty, and digital learning resources."
		else:
			if lang == 'mr':
				reply = "मी करिअर, अभ्यास किंवा दिव्या क्लासेसबद्दल मदत करू शकते. प्रेरणादायी विचार, अभ्यास टिप्स किंवा गणिती मदत विचारू शकता!"
			else:
				reply = "I'm here to help with career, study, and Divya Classes questions. You can also ask for motivational quotes, study tips, or simple math help!"
		return JsonResponse({'success': True, 'reply': reply})
	return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)
from django.shortcuts import render






from .models import Enquiry, LectureVideo, Testimonial, Faculty

# Home page view
def home(request):
	videos = LectureVideo.objects.order_by('-uploaded_at')
	testimonials = Testimonial.objects.order_by('-created_at')[:6]
	faculty = Faculty.objects.all()
	return render(request, 'index.html', {
		'videos': videos,
		'testimonials': testimonials,
		'faculty': faculty,
	})

@csrf_exempt
def enquiry(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		standard = request.POST.get('standard')
		message = request.POST.get('message')
		enquiry = Enquiry.objects.create(
			name=name,
			email=email,
			phone=phone,
			standard=standard,
			message=message
		)
		return JsonResponse({'success': True})
	return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)
