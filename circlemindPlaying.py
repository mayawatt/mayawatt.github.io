from circlemind import Circlemind

# Initialize the client
sophie = Circlemind()

sophie.add("Sophie enjoys hiking in the Italian Alps.")

res = sophie.query("Where does Sophie like the hike?")

print(res.response)
