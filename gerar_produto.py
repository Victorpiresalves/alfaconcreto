"""Gera produto.html no visual novo (mesma identidade do index.html: cinza-concreto, grafite, azul da logo; Manrope +
IBM Plex Mono; sem emojis). Os dados dos 69 produtos ficam em produtos.js (bloco original, sem alteração de conteúdo).
Uso: python3 gerar_produto.py  (na raiz do repositório)
"""
dados = open('produtos.js', encoding='utf-8').read()

pagina = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title id="pageTitle">Produto · Alfa Soluções em Concreto</title>
<meta name="description" id="pageDesc" content="Produto em concreto pré-moldado da Alfa Soluções em Concreto, Araçatuba-SP.">
<link rel="icon" href="img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root { --concreto:#ECEAE6; --linha:#D3CFC7; --grafite:#1E2226; --texto:#3B4046; --suave:#6E737A;
        --azul:#0B3F78; --azul-2:#06549D; --verde:#019460; --branco:#FAF9F7; }
*,*::before,*::after { box-sizing:border-box; margin:0; padding:0 }
body { font-family:'Manrope',system-ui,sans-serif; background:var(--concreto); color:var(--texto); line-height:1.6; -webkit-font-smoothing:antialiased }
img { display:block; max-width:100% } a { color:inherit; text-decoration:none }
.mono { font-family:'IBM Plex Mono',monospace; font-size:.78rem; letter-spacing:.06em; text-transform:uppercase; color:var(--suave) }
.wrap { max-width:1240px; margin:0 auto; padding:0 28px }
h1,h2,h4 { color:var(--grafite); letter-spacing:-.02em; line-height:1.08; font-weight:800 }
.btn { display:inline-flex; align-items:center; justify-content:center; gap:10px; padding:16px 26px; font-weight:700; font-size:.95rem; border-radius:2px; transition:.2s }
.btn-azul { background:var(--azul); color:#fff } .btn-azul:hover { background:var(--azul-2) }
.btn-linha { border:1.5px solid var(--grafite); color:var(--grafite) } .btn-linha:hover { background:var(--grafite); color:#fff }
.btn-wa { background:var(--verde); color:#fff } .btn-wa:hover { filter:brightness(1.08) }
header { position:sticky; top:0; z-index:50; background:rgba(236,234,230,.92); backdrop-filter:blur(10px); border-bottom:1px solid var(--linha) }
.nav { display:flex; align-items:center; justify-content:space-between; height:78px }
.nav img { height:52px; width:auto }
.nav nav { display:flex; gap:34px; align-items:center; font-weight:600; font-size:.92rem }
.nav nav a:not(.btn):hover { color:var(--azul) } .nav .btn { padding:12px 20px }
.trilha { padding:28px 0 0 } .trilha a:hover { color:var(--azul) } .trilha span { margin:0 8px }

.produto { display:grid; grid-template-columns:1.1fr 1fr; gap:64px; padding:28px 0 110px; align-items:start }
.foto { background:#fff; border:1px solid var(--linha); aspect-ratio:1; overflow:hidden; position:sticky; top:104px }
.foto img { width:100%; height:100%; object-fit:cover }
.info h1 { font-size:clamp(2.2rem,4vw,3.4rem); margin:14px 0 22px }
.info .desc { font-size:1.08rem; max-width:520px }
.ficha { margin-top:40px; border-top:1px solid var(--grafite) }
.ficha .mono { display:block; padding:16px 0 6px }
.ficha li { list-style:none; display:flex; gap:16px; padding:14px 0; border-bottom:1px solid var(--linha); color:var(--grafite); font-weight:600 }
.ficha li::before { content:attr(data-n); font-family:'IBM Plex Mono',monospace; font-size:.8rem; color:var(--suave); font-weight:400; padding-top:2px; min-width:24px }
.acoes { display:flex; gap:12px; margin-top:36px; flex-wrap:wrap }
.passos { margin-top:44px; display:grid; grid-template-columns:repeat(3,1fr); gap:18px; border-top:1px solid var(--linha); padding-top:22px }
.passos div { font-size:.88rem } .passos b { display:block; color:var(--grafite); margin-top:4px }

.rel { padding:100px 0 120px; border-top:1px solid var(--linha) }
.rel-head { display:flex; justify-content:space-between; align-items:end; gap:20px; margin-bottom:34px; flex-wrap:wrap }
.rel h2 { font-size:clamp(1.8rem,3vw,2.5rem); margin-top:8px }
.rel-head a { font-weight:700; color:var(--azul) }
.grade { display:grid; grid-template-columns:repeat(4,1fr); gap:1px; background:var(--linha); border:1px solid var(--linha) }
.prod { background:var(--branco); display:flex; flex-direction:column; transition:background .2s }
.prod:hover { background:#fff }
.prod .ft { aspect-ratio:1; overflow:hidden; background:#fff }
.prod .ft img { width:100%; height:100%; object-fit:cover; transition:transform .5s }
.prod:hover .ft img { transform:scale(1.04) }
.prod .tx { padding:18px 20px 22px; display:flex; justify-content:space-between; gap:12px; align-items:flex-end; flex:1 }
.prod h4 { font-size:1rem; font-weight:700; line-height:1.3; margin-top:6px }
.prod .seta { font-size:1.2rem; color:var(--azul) }

.nao { padding:140px 0; text-align:center } .nao h1 { font-size:2.4rem; margin:14px 0 16px } .nao .btn { margin-top:28px }

.contato { background:var(--grafite); color:#C9CDD2; padding:70px 0 }
.contato .wrap { display:flex; justify-content:space-between; gap:40px; flex-wrap:wrap; align-items:center }
.contato h2 { color:#fff; font-size:clamp(1.6rem,2.6vw,2.2rem); max-width:560px }
.contato p { margin-top:10px }
footer { background:var(--grafite); color:#8D939A; border-top:1px solid #3A3F45; padding:28px 0; font-size:.85rem }
footer .wrap { display:flex; justify-content:space-between; gap:20px; flex-wrap:wrap }
.wa-fixo { position:fixed; right:22px; bottom:22px; width:58px; height:58px; border-radius:50%; background:var(--verde); display:grid; place-items:center; box-shadow:0 8px 24px rgba(0,0,0,.18); z-index:60 }
.wa-fixo svg { width:30px; height:30px; fill:#fff }

@media (max-width:1020px) { .produto { grid-template-columns:1fr; gap:36px } .foto { position:static } .grade { grid-template-columns:repeat(3,1fr) } }
@media (max-width:640px) {
  .wrap { padding:0 18px } .nav nav a:not(.btn) { display:none } .nav img { height:42px }
  .produto { padding-bottom:70px } .passos { grid-template-columns:1fr; gap:10px } .grade { grid-template-columns:1fr 1fr }
  .acoes .btn { width:100% } .prod .tx { padding:14px } .rel { padding:70px 0 }
}
</style>
</head>
<body>

<header><div class="wrap nav">
  <a href="index.html"><img src="img/logo.png" alt="Alfa Soluções em Concreto"></a>
  <nav><a href="index.html#linhas">Linhas</a><a href="index.html#catalogo">Catálogo</a><a href="index.html#como-pedir">Como pedir</a><a href="index.html#sobre">Sobre</a>
    <a class="btn btn-azul" id="navWa" href="https://wa.me/5518997603980" target="_blank" rel="noopener">Pedir orçamento</a></nav>
</div></header>

<main class="wrap" id="produtoPage">
  <div class="trilha mono"><a href="index.html">Início</a><span>/</span><a href="index.html#catalogo" id="trilhaCat">Catálogo</a><span>/</span><b id="trilhaNome"></b></div>
  <div class="produto">
    <div class="foto"><img id="prodImg" src="" alt=""></div>
    <div class="info">
      <span class="mono" id="prodCat"></span>
      <h1 id="prodNome"></h1>
      <p class="desc" id="prodDesc"></p>
      <div class="ficha"><span class="mono">Características</span><ul id="prodCaracts"></ul></div>
      <div class="acoes">
        <a class="btn btn-wa" id="prodWa" href="#" target="_blank" rel="noopener">Pedir orçamento deste produto</a>
        <a class="btn btn-linha" href="index.html#catalogo">Ver catálogo completo</a>
      </div>
      <div class="passos">
        <div><span class="mono">01</span><b>Escolha o modelo</b></div>
        <div><span class="mono">02</span><b>Envie as medidas</b></div>
        <div><span class="mono">03</span><b>Receba o orçamento</b></div>
      </div>
    </div>
  </div>
</main>

<section class="rel" id="relSection" style="display:none"><div class="wrap">
  <div class="rel-head"><div><span class="mono">Da mesma linha</span><h2 id="relTitulo"></h2></div><a href="index.html#catalogo">Ver todos →</a></div>
  <div class="grade" id="relGrade"></div>
</div></section>

<section class="contato"><div class="wrap">
  <div><span class="mono">Contato</span><h2>Ficou com dúvida sobre medidas ou acabamento?</h2>
    <p>R. Antônio Afonso de Toledo, 369 · Jardim Sumaré, Araçatuba-SP · Seg. a sex., 7h às 17h</p></div>
  <a class="btn btn-wa" id="ctWa" href="https://wa.me/5518997603980" target="_blank" rel="noopener">Falar no WhatsApp</a>
</div></section>

<footer><div class="wrap"><span>© 2026 Alfa Soluções em Concreto · Araçatuba-SP</span><span>(18) 99760-3980 · (18) 99676-9650</span></div></footer>

<a class="wa-fixo" id="fixoWa" href="https://wa.me/5518997603980" target="_blank" rel="noopener" aria-label="WhatsApp"><svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.4-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.2c0-.1-.2-.2-.4-.3z"/></svg></a>

<script>
''' + dados + '''

const LINHA = { 'area-lazer':'Área e Lazer', 'revestimento':'Revestimento 3D', 'elemento-vazado':'Elemento Vazado',
                'acabamento':'Acabamento', 'construcao-civil':'Construção Civil' };
const $ = id => document.getElementById(id);
const id = new URLSearchParams(location.search).get('id');
const p = produtos[id];
if (!p) {
  $('produtoPage').innerHTML = '<div class="nao"><span class="mono">Catálogo</span><h1>Produto não encontrado</h1>' +
    '<p>O produto que você procura não existe ou foi removido.</p><a class="btn btn-azul" href="index.html#catalogo">Ver catálogo</a></div>';
} else {
  const linha = LINHA[p.catId] || p.cat;
  $('pageTitle').textContent = p.nome + ' · Alfa Soluções em Concreto';
  $('pageDesc').content = (p.desc || '').substring(0, 160);
  $('trilhaCat').textContent = linha; $('trilhaNome').textContent = p.nome;
  $('prodImg').src = p.img; $('prodImg').alt = p.nome;
  $('prodCat').textContent = linha; $('prodNome').textContent = p.nome; $('prodDesc').textContent = p.desc || '';
  $('prodCaracts').innerHTML = (p.caracts || []).map((c, i) => `<li data-n="${String(i + 1).padStart(2, '0')}">${c}</li>`).join('');
  const wa = 'https://wa.me/5518997603980?text=' + encodeURIComponent('Olá! Vim pelo site e gostaria de um orçamento para: ' + p.nome);
  ['prodWa', 'navWa', 'ctWa', 'fixoWa'].forEach(k => $(k).href = wa);
  const rel = Object.entries(produtos).filter(([k, v]) => v.catId === p.catId && k !== id).slice(0, 8);
  if (rel.length) {
    $('relSection').style.display = '';
    $('relTitulo').textContent = 'Outros produtos de ' + linha;
    $('relGrade').innerHTML = rel.map(([k, v]) => `<a class="prod" href="produto.html?id=${k}">
      <div class="ft"><img src="${v.img}" alt="${v.nome}" loading="lazy"></div>
      <div class="tx"><div><span class="mono">${linha}</span><h4>${v.nome}</h4></div><span class="seta">→</span></div></a>`).join('');
  }
}
</script>
</body>
</html>
'''
open('produto.html', 'w', encoding='utf-8').write(pagina)
print('ok')
