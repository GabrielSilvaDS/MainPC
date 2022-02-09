function carregar (){
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    var minuto = data.getMinutes()
    if (hora >= 0 && hora < 12){
        msg.innerHTML = `Agora são ${hora}:${minuto} Bom Dia !!`
        img.src = 'dia.png'
        document.body.style.background = '#b98a43'
    } else if (hora >= 12 && hora < 18){
        msg.innerHTML = `Agora são ${hora}:${minuto} Boa Tarde !!`
        img.src = 'tarde.png'
        document.body.style.background = '#745381'
    } else {
        msg.innerHTML = `Agora são ${hora}:${minuto} Boa Noite !!`
        img.src = 'noite.png'
        document.body.style.background = '#4e4343'
    }
}