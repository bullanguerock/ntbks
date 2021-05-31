console.log('hello world')
const url = window.location.href
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const resultsBox = document.getElementById('results-box')
const ramInput = document.getElementById('ram-input')

var q = searchInput.value
var ramq = ramInput.value


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

const sendSearchData = (query, ram)=> {
    $.ajax({        
        type :'POST',
        url :'ntbks/search/',
        data: {
            'csrfmiddlewaretoken' : csrf,
            'query' : query,
            'ram' : ram,
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
    q = e.target.value
    console.log(q)
    delayKeyUp(() => {sendSearchData(q, ramq)}, 1000);
})

ramInput.addEventListener('keyup', e=>{
    ramq = e.target.value
    console.log(ramInput)
    delayKeyUp(() => {sendSearchData(q, ramq)}, 1000);
})