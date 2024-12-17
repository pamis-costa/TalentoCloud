const titulo = document.getElementById("titulo");
const listaNaoOrdenada = document.querySelector("ul");
const link = document.querySelector("a");
const listaOrdenada = document.getElementById ("lista-ordenada");

// .innerText
titulo.innerText = "Bem-vindo a esse Projeto";
link.innerText = "Visite o site da Proz Educação";

// .innerHTML
listaNaoOrdenada.innerHTML = `
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
`;

listaOrdenada.innerHTML = `
    <li><a href="https://www.google.com" target="_blank">Google</a></li>
    <li><a href="https://www.youtube.com" target="_blank">YouTube</a></li>
    <li><a href="https://github.com" target="_blank">GitHub</a></li>
`;