import smtplib
gmail_user = 'shubhamchoubey447@gmail.com'  
gmail_password = '*******'


def send_mail(to,subject,body):
	sent_from = gmail_user  

	email_text = "{}".format(body)

	try:  
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(gmail_user, gmail_password)
		server.sendmail(sent_from, to, email_text)
		server.close()

		print('Email sent!')
	except:  
		print('Something went wrong...')
