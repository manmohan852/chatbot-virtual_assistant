import speech_recognition as sr
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone Name: \"{1}\".\tDevice_index= {0})".format(index, name))
    #print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
    
