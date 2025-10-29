from flask import Flask, jsonify, request

app = Flask(__name__)

playlist = [
    {"id": 1, "titulo": "Material Girl", "artista": "Madonna", "duracao": 255, "url": "teste.com"},
    {"id": 2, "titulo": "Breath (In The Air)", "artista": "Pink Floyd", "duracao": 255, "url": "teste.com"},
]

@app.route('/musicas', methods=['GET'])
def get_musicas():
    return jsonify({"playlist": playlist, "total": len(playlist)})

@app.route('/musicas', methods=['POST'])
def add_musica():
    nova_musica = request.json
    
    nova_musica["id"] = len(playlist) +1

    playlist.append(nova_musica)
    return jsonify({"mensagem": "Música adicionada!", "musica": nova_musica}), 201

@app.route("/musicas/<int:id>", methods=["GET"])
def get_musica_by_id(id):
    for musica in playlist:
        if musica["id"] == id:
            return jsonify({"mensagem": "A música foi encontrada!", "musica": musica})
        
    return jsonify({"mensagem": "Música não encontrada!"}), 404

@app.route("/musicas/<int:id>", methods=["PUT"])
def update_musica(id):
    dados = request.json

    for musica in playlist:
        if musica["id"] == id:
            musica.update(dados)
            return jsonify({"mensagem": "Música atualizada!", "musica": musica})
        
    return jsonify({"erro": "Música n]ao encontrada!"}), 404

@app.route("/musicas/<int:id>", methods=["DELETE"])
def delete_musica(id):
    for musica in playlist:
        if musica["id"] == id:
            playlist.remove(musica)
            return jsonify({"mensagem": "Música deletada!"}), 200
        
    return jsonify({"erro": "Música não encontrada!"}), 404

if __name__ == '__main__':
    app.run(debug=True)