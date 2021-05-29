console.log('hello world')
const url = window.location.href
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const resultsBox = document.getElementById('results-box')

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
console.log(csrf)

const sendSearchData = (game)=> {
    $.ajax({
        type :'POST',
        url :'ajax/search/',
        data: {
            'csrfmiddlewaretoken' : csrf,
            'game' : game,
        },
        success: (res)=> {
            console.log(res.data);
            const data = res.data
            if (Array.isArray(data)) {
                resultsBox.classList.remove('not-visible')
                resultsBox.innerHTML = ""
                data.forEach(game =>{               
                    resultsBox.innerHTML += `
                        <div class="container">
                            <img src="${game.img}">
                            <p>${game.nombre}<p><br>
                            <p>${game.precio}<p><br>
                        </div>
                    `
                })
            }else {
                if (searchInput.value.length > 0) {
                    resultsBox.innerHTML = `
                    <p>${data}<p><br>
                `
                } else {
                    resultsBox.classList.add('not-visible')
                }
            }
        },
        error: (err)=> {
            console.log(err)
        }
    })
}

searchInput.addEventListener('keyup', e=>{
    console.log(e.target.value)

    sendSearchData(e.target.value)
})