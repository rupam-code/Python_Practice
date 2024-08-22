import urllib.request as urllib
def min(url):
    print("Cheking Connectivity")

    response= urllib.urlopen(url)
    print("Connected to ",url,"Successfully")
    print("The respose code was",response.getcode())

print("This is a site Connectivity Cheker Porgram---")
input_url=input("Input the URL of the site you want to check= ")

min(input_url)