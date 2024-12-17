const titulo = document.createElement("h1");
titulo.id = "titulo";
titulo.textContent = "Loja Virtual - Produtos Incríveis!";
document.body.appendChild(titulo);

const produto = document.createElement("div");
produto.id = "produto";

const nomeProduto = document.createElement("h2");
nomeProduto.textContent = "Mesa digitalizadora";

const descricaoProduto = document.createElement("p");
descricaoProduto.textContent = "Realize seus desenhos digitalmente com essa mega mesa digitalizadora";

const precoProduto = document.createElement("p");
precoProduto.textContent = "R$ 1.199.90";

const imagemProduto = document.createElement("img");
imagemProduto.src = "https://cdn.awsli.com.br/800x800/2116/2116743/produto/245102632/3-upmbzpxw8g.png";
imagemProduto.alt = "Imagem da mesa digitalizadora";


produto.appendChild(nomeProduto);
produto.appendChild(descricaoProduto);
produto.appendChild(precoProduto);
produto.appendChild(imagemProduto);

document.body.appendChild(produto);