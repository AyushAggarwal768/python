###############################################################################

#Q.1- What is an access token? 
#Generate your access token for any API.(for example Twitter,Spotify etc). 

'''
Access Token
The Access Token is a credential that can be used by an application to access an API.

*to generate access token

1.>create a twitter account
2.>go to apps.twitter.com
3.>click on create new application
4.>fill the form
5.>click on create new application
6.>note the consumer_key,consumer_secrate,access_token,access_token_secrate
'''

###############################################################################

#Q.2- Get the IP address of some common sites like Google, Facebook by using DNS lookup.

'''
nslookup google.com
Server:  google-public-dns-a.google.com
Address:  8.8.8.8

Non-authoritative answer:
DNS request timed out.
    timeout was 2 seconds.
Name:    google.com
Address:  172.217.24.238

nslookup facebook.com
Server:  UnKnown
Address:  2405:200:800::1

Non-authoritative answer:
Name:    facebook.com
Addresses:  2a03:2880:f12f:83:face:b00c:0:25de
          157.240.16.35


>nslookup twitter.com
Server:  UnKnown
Address:  2405:200:800::1

Non-authoritative answer:
Name:    twitter.com
Addresses:  104.244.42.193
            104.244.42.65
'''

###############################################################################

#Q.4- What is a difference between library and API.Figure it out with examples.

'''
A library 
	is a collection of functions / objects that serves one particular purpose.
	 you could use a library in a variety of projects. 
	(Various specialized services in our case)

	ex: JQuery library, is a library of prewritten,
	 cross-browser Javascript animations and functions 
	which you will need while making a website.


An API 
	is an interface for other programs to interact with your program or library 
	 without having direct access.
	 ( giving specifications for our need to various vendors in our case)

	ex: with Google Map APIs you can show maps for different places without 
	writing/hosting the whole code on your server, and just use it,
	 usually this data transfer is in form of JSON i.e JavaScript Object Notation.
'''

###############################################################################
