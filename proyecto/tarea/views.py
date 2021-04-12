from django.http import HttpResponse
from django.shortcuts import render
import requests


def index(request):
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters?category=Better+Call+Saul')
    response1 = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters')
    personajes = response.json()
    personajes1 = response1.json()
    capitulos = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes')
    valores = capitulos.json()[len(capitulos.json())-1]
    breaking_bad = []
    better_call_saul = []
    for elemento in capitulos.json():
    	if elemento['series'] == 'Better Call Saul':
    		better_call_saul.append(elemento)
    	else:
    		breaking_bad.append(elemento)

    diccionario_temporadas = {'bb':int(breaking_bad[len(breaking_bad)-1]['season']),'bcs':int(better_call_saul[len(better_call_saul)-1]['season'])}
    temporadasbb = [i for i in range(diccionario_temporadas['bb']+1)]
    temporadasbcs = [i for i in range(diccionario_temporadas['bcs']+1)]
    temporadasbcs.pop(0)
    temporadasbb.pop(0)
    return render(request, 'tarea/index.html', {'llave':capitulos.json(), 'valores':capitulos, 'temporadasbb':temporadasbb, 'temporadasbcs':temporadasbcs})
def temporadabb(request, season):
    capitulos = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes')
    return render(request, 'tarea/Temporadas.html', {'llave':capitulos.json(), 'temporada':str(season), 'serie':'Breaking Bad'})
def temporadabcs(request, season):
    capitulos = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes')
    return render(request, 'tarea/Temporadas.html', {'llave':capitulos.json(), 'temporada':str(season), 'serie':'Better Call Saul'})

def episodios(request,chapter):
	capitulos = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes/')
	capitulo = 0
	for elemento in capitulos.json():
		if elemento['episode_id'] == chapter:
			capitulo = elemento


	return render(request, 'tarea/episodios.html', {'episode_id':capitulo['episode_id'],'title':capitulo['title'],'season':capitulo['season'],
		'air_date':capitulo['air_date'][0:10],'characters':capitulo['characters'],'episode':capitulo['episode'],'series':capitulo['series']})

def personajes(request,personaje):
	nombre = personaje.split(' ')
	character = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+nombre[0]+'+'+nombre[1])
	character = character.json()[0]
	return render(request,'tarea/personajes.html',{'nombre':character['name'], 'ocupacion':character['occupation'],'status':character['status'],'sobrenombres':character['nickname'],
	 'actor':character['portrayed'], 'imagen':character['img'], 'tbb':character['appearance'], 'tbcs':character['better_call_saul_appearance']})

# Create your views here.
