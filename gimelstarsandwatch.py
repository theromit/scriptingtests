url = 'https://api.github.com'
pathstar = '/repos/paypal/gimel/stargazers'
pathevent = '/repos/paypal/gimel/events'

star = requests.get(url+pathstar)
event = requests.get(url+pathevent)

starcount = 0
eventcount = 0
watchcount = 0
forkcount = 0

#print (star.links['next']['url'])
print (star.links['last']['url'])
maxstarpages = int(star.links['last']['url'][star.links['last']['url'].find("=")+1:])
print (maxstarpages)

#print (event.links['next']['url'])
print (event.links['last']['url'])
maxeventpages = int(event.links['last']['url'][event.links['last']['url'].find("=")+1:])
print (maxeventpages)

for s in range(0, maxstarpages):
    if s+1 == 1:
        starurl = url+pathstar
    else:
        starurl = url+pathstar+"?page="+str(s+1)
    su = requests.get(starurl).json()
    for n in range(len(su)):
        starcount += 1
        print("Starred by: ", su[n]['login'])
print("\n", "Total stars: ", starcount)
        
for e in range(0, maxeventpages):
    if e+1 == 1:
        eventurl = url+pathevent
    else:
        eventurl = url+pathevent+"?page="+str(e+1)
    ev = requests.get(eventurl).json()
    for e in range(len(ev)):
        eventcount += 1
        #print("Event: ", ev[e]['actor']['login'], " ", ev[e]['type'])
    for f in range(len(ev)):
        if ev[f]['type'] == 'ForkEvent':
            forkcount += 1
            print("Fork: ", ev[f]['actor']['login'])
        if ev[f]['type'] == 'WatchEvent':
            watchcount += 1
            print("Watch: ", ev[f]['actor']['login'])
            
print ("\n", "Total forks: ", forkcount)

print ("\n", "Total watched: ", watchcount)

print ("\n", "Total events: ", eventcount)
