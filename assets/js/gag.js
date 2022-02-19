document.querySelector("button").addEventListener("click",function (e){
    e.preventDefault()

    fetch("/gag/").then(s => s.text()).then(r => {
        document.querySelector("span").innerHTML=`Info`
    })
})

document.querySelectorAll(".categories > a").forEach((item) => {
    item.addEventListener("click",  function (event){
        event.preventDefault()
        item.style.color=`blue`
        // document.querySelector("#post").innerHTML=`${this.innerHTML}`
    })
})

document.querySelectorAll(".categories > a").forEach((item) =>{
    item.style.color=`black`
})