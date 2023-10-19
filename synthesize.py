from ttsmms import TTS

tts=TTS(r'C:\Users\enisk\Desktop\tts\data\kmr-script_latin') # or "model_dir_path" your path dir that extract a tar ball archive
#wav=tts.synthesis("bê guman, enîs. kurdî zimanekî kevn û berfireh e ku li ser axa Mezopotamyayê bi hezaran salan e hatiye axaftin. ev ziman, wekî çavkanîyên deryayên frat û dîcleyê, her tim bûye şahîdê dîroka gelê kurd. bi vê re, kurdî jî yek ji zimanên ku di warê teknolojiyê de hêj neqasî hatiye bikaranîn. ji bo vê yekê, projeyên wekî yên te, yên ku alîkariya ziman û çandê dikin, gelekî girîng in.")
# output:
# {
#    "x":array(wav array),
#    "sampling_rate": 16000
# }

tts.synthesis("bê guman, enîs. kurdî zimanekî kevn û berfireh e ku li ser axa Mezopotamyayê bi hezaran salan e hatiye axaftin. ev ziman, wekî çavkanîyên deryayên frat û dîcleyê, her tim bûye şahîdê dîroka gelê kurd. bi vê re, kurdî jî yek ji zimanên ku di warê teknolojiyê de hêj neqasî hatiye bikaranîn. ji bo vê yekê, projeyên wekî yên te, yên ku alîkariya ziman û çandê dikin, gelekî girîng in.")
# output: example.wav file

