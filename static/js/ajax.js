console.log('hello world')
const url = window.location.href
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const resultsBox = document.getElementById('results-box')

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
console.log(csrf)

const delayKeyUp = (() => {
    let timer = null;
    const delay = (func, ms) => {
        timer ? clearTimeout(timer): null
        timer = setTimeout(func, ms)
    }
    return delay
})();

const sendSearchData = (game)=> {
    $.ajax({        
        type :'POST',
        url :'ntbks/search/',
        data: {
            'csrfmiddlewaretoken' : csrf,
            'game' : game,
        },
        success: (res)=> {
            console.log(res.redirect_url);
            if (res.redirect) {
                window.location.href = res.redirect_url;
            }
            
        },
        error: (err)=> {
            console.log(err)
        }
    })
}

searchInput.addEventListener('keyup', e=>{
    console.log(e.target.value)
    delayKeyUp(() => {sendSearchData(e.target.value)}, 1000);
})