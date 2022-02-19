function load_data(url) {
    $("#post").html("Loading...")

    fetch(url + "?is_ajax=1").then(r => r.text()).then((data) => {
        window.history.pushState({}, "", url)

        $("#post").html(data).children(".pagi").on("click", function () {
            load_data($(this).attr('href'))
            return false

        })

    });
}
$(".categories a").on("click", function () {
    load_data($(this).attr('href'))
    return false

})



// img = document.querySelector(".postimg img")
// document.querySelectorAll("a.cat").forEach((item) => {
//     item.addEventListener("click",function (event){
//         event.preventDefault()
//         document.querySelector("#post").innerHTML=`${item.innerHTML}`
//         document.querySelector(".postid").innerHTML = item.getAttribute("data-id")
//         img.setAttribute("style", item.getAttribute("data-style"))
//         document.querySelectorAll(".d-none").forEach((e) =>{
//             e.classList.remove("d-none")
//         })
//     })
// })