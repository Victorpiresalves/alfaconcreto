"""Gera index.html (redesign Alfa Soluções em Concreto, 28/10/2026).
Direção: estúdio de arquitetura, não template — cinza-concreto + grafite + azul-marinho da logo (#06549D) e o verde da
logo (#019460) só como acento/WhatsApp; Manrope + IBM Plex Mono para medidas/especificações; sem emojis, sem números
inventados. Catálogo = os 69 produtos do index.html atual (mesmos ids → produto.html continua funcionando).
Uso: python3 gerar_index.py  (na raiz do repositório; catálogo em catalogo.json)
"""
import re, json, html

prods = json.load(open('catalogo.json', encoding='utf-8'))   # 69 produtos (extraídos do site antigo em 28/10/2026)
CAT = {'area-lazer': 'Área e Lazer', 'revestimento': 'Revestimento 3D', 'elemento-vazado': 'Elemento Vazado',
       'acabamento': 'Acabamento', 'construcao-civil': 'Construção Civil'}
cont = {k: sum(p['c'] == k for p in prods) for k in CAT}
capa = {k: next(p for p in prods if p['c'] == k)['i'] for k in CAT}
capa['revestimento'] = next(p['i'] for p in prods if p['n'] == 'Floral')
capa['elemento-vazado'] = next(p['i'] for p in prods if p['n'] == 'Mandala')
DESC = {'area-lazer': 'Mesas, bancos, pergolados e cubas para jardins, praças e áreas gourmet.',
        'revestimento': 'Placas 3D que transformam paredes lisas em superfícies com relevo e sombra.',
        'elemento-vazado': 'Cobogós que filtram a luz e ventilam sem perder privacidade.',
        'acabamento': 'Pisos, guias, capas de muro e peças de acabamento para a obra.',
        'construcao-civil': 'Casas de gás, caixas, degraus e peças técnicas sob medida.'}
WA = 'https://wa.me/5518997603980?text=' + 'Olá! Vim pelo site e gostaria de um orçamento.'.replace(' ', '%20')

linhas = '\n'.join(f'''      <a class="linha" href="#catalogo" data-filtro="{k}">
        <div class="linha-img"><img src="{capa[k]}" alt="{CAT[k]}" loading="lazy"></div>
        <div class="linha-txt"><span class="mono">{i+1:02d} · {cont[k]} produtos</span><h3>{CAT[k]}</h3><p>{DESC[k]}</p></div>
      </a>''' for i, k in enumerate(CAT))
abas = '\n'.join([f'        <button class="aba ativa" data-cat="todos">Todos <span>{len(prods)}</span></button>'] +
                 [f'        <button class="aba" data-cat="{k}">{CAT[k]} <span>{cont[k]}</span></button>' for k in CAT])

pagina = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Alfa Soluções em Concreto · Pré-moldados em Araçatuba-SP</title>
<meta name="description" content="Revestimentos 3D, elementos vazados, mesas, bancos e peças em concreto pré-moldado, sob medida. Fábrica em Araçatuba-SP. {len(prods)} produtos no catálogo.">
<link rel="icon" href="img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root {{ --concreto:#ECEAE6; --concreto-2:#E2DFD9; --linha:#D3CFC7; --grafite:#1E2226; --texto:#3B4046; --suave:#6E737A;
        --azul:#0B3F78; --azul-2:#06549D; --verde:#019460; --branco:#FAF9F7; }}
*,*::before,*::after {{ box-sizing:border-box; margin:0; padding:0 }}
html {{ scroll-behavior:smooth }}
body {{ font-family:'Manrope',system-ui,sans-serif; background:var(--concreto); color:var(--texto); line-height:1.6; -webkit-font-smoothing:antialiased }}
img {{ display:block; max-width:100% }}
a {{ color:inherit; text-decoration:none }}
.mono {{ font-family:'IBM Plex Mono',monospace; font-size:.78rem; letter-spacing:.06em; text-transform:uppercase; color:var(--suave) }}
.wrap {{ max-width:1240px; margin:0 auto; padding:0 28px }}
h1,h2,h3 {{ color:var(--grafite); letter-spacing:-.02em; line-height:1.08; font-weight:800 }}
h2 {{ font-size:clamp(2rem,4vw,3.1rem) }}
.btn {{ display:inline-flex; align-items:center; gap:10px; padding:16px 26px; font-weight:700; font-size:.95rem; border-radius:2px; transition:.2s }}
.btn-azul {{ background:var(--azul); color:#fff }} .btn-azul:hover {{ background:var(--azul-2) }}
.btn-linha {{ border:1.5px solid var(--grafite); color:var(--grafite) }} .btn-linha:hover {{ background:var(--grafite); color:#fff }}
.btn-wa {{ background:var(--verde); color:#fff }} .btn-wa:hover {{ filter:brightness(1.08) }}

/* topo */
header {{ position:sticky; top:0; z-index:50; background:rgba(236,234,230,.92); backdrop-filter:blur(10px); border-bottom:1px solid var(--linha) }}
.nav {{ display:flex; align-items:center; justify-content:space-between; height:78px }}
.nav img {{ height:52px; width:auto }}
.nav nav {{ display:flex; gap:34px; align-items:center; font-weight:600; font-size:.92rem }}
.nav nav a:not(.btn):hover {{ color:var(--azul) }}
.nav .btn {{ padding:12px 20px }}

/* hero */
.hero {{ display:grid; grid-template-columns:1.05fr 1fr; min-height:min(calc(100vh - 78px), 820px); border-bottom:1px solid var(--linha) }}
.hero-txt {{ padding:9vh 56px 8vh 0; display:flex; flex-direction:column; justify-content:center; padding-left:max(28px, calc((100vw - 1240px)/2 + 28px)) }}
.hero h1 {{ font-size:clamp(2.6rem,5.4vw,4.9rem); margin:22px 0 26px }}
.hero h1 em {{ font-style:normal; color:var(--azul) }}
.hero p.lead {{ font-size:1.12rem; max-width:520px; color:var(--texto) }}
.hero .acoes {{ display:flex; gap:14px; margin-top:38px; flex-wrap:wrap }}
.fatos {{ display:grid; grid-template-columns:repeat(4,auto); gap:0; margin-top:56px; border-top:1px solid var(--linha) }}
.fatos div {{ padding:18px 22px 0 0 }}
.fatos b {{ display:block; font-size:1.35rem; color:var(--grafite); font-weight:800 }}
.hero-img {{ position:relative; overflow:hidden }}
.hero-img img {{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 35% }}
.hero-img figcaption {{ position:absolute; left:20px; bottom:18px; background:rgba(250,249,247,.92); padding:8px 12px }}

/* seções */
section {{ padding:120px 0; border-bottom:1px solid var(--linha) }}
.sec-head {{ display:grid; grid-template-columns:1fr 1fr; gap:60px; align-items:end; margin-bottom:64px }}
.sec-head p {{ max-width:460px; justify-self:end; color:var(--texto) }}

/* linhas */
.linhas {{ display:grid; grid-template-columns:repeat(5,1fr); border-top:1px solid var(--linha); border-left:1px solid var(--linha) }}
.linha {{ border-right:1px solid var(--linha); border-bottom:1px solid var(--linha); background:var(--branco); transition:.25s }}
.linha:hover {{ background:#fff }}
.linha-img {{ aspect-ratio:1; overflow:hidden; background:#fff }}
.linha-img img {{ width:100%; height:100%; object-fit:cover; transition:transform .6s }}
.linha:hover .linha-img img {{ transform:scale(1.05) }}
.linha-txt {{ padding:22px 22px 28px }}
.linha h3 {{ font-size:1.25rem; margin:8px 0 8px }}
.linha p {{ font-size:.9rem; color:var(--suave) }}

/* ambientes */
.amb {{ display:grid; grid-template-columns:1.3fr 1fr 1fr; gap:18px }}
.amb figure {{ position:relative; overflow:hidden; background:var(--concreto-2) }}
.amb img {{ width:100%; height:100%; object-fit:cover; aspect-ratio:3/4 }}
.amb figcaption {{ padding:16px 2px 0 }}
.amb figcaption b {{ display:block; color:var(--grafite); font-size:1.05rem }}
.nota {{ margin-top:22px }}

/* antes x depois */
.antes {{ display:grid; grid-template-columns:1fr 1fr; gap:18px; margin-top:80px }}
.antes figure {{ position:relative }}
.antes .mono {{ position:absolute; top:16px; left:16px; background:var(--branco); padding:6px 10px; color:var(--grafite) }}
.antes img {{ aspect-ratio:4/5; object-fit:cover; width:100% }}

/* catálogo */
.abas {{ display:flex; gap:6px; flex-wrap:wrap; margin-bottom:34px }}
.aba {{ font:600 .9rem 'Manrope',sans-serif; background:none; border:1px solid var(--linha); color:var(--texto); padding:11px 18px; cursor:pointer; border-radius:2px; transition:.2s }}
.aba span {{ font-family:'IBM Plex Mono',monospace; font-size:.75rem; color:var(--suave); margin-left:6px }}
.aba:hover {{ border-color:var(--grafite) }}
.aba.ativa {{ background:var(--grafite); border-color:var(--grafite); color:#fff }} .aba.ativa span {{ color:#bfc3c8 }}
.grade {{ display:grid; grid-template-columns:repeat(4,1fr); gap:1px; background:var(--linha); border:1px solid var(--linha) }}
.prod {{ background:var(--branco); display:flex; flex-direction:column; transition:background .2s }}
.prod:hover {{ background:#fff }}
.prod .ft {{ aspect-ratio:1; overflow:hidden; background:#fff }}
.prod .ft img {{ width:100%; height:100%; object-fit:cover; transition:transform .5s }}
.prod:hover .ft img {{ transform:scale(1.04) }}
.prod .tx {{ padding:18px 20px 22px; display:flex; justify-content:space-between; gap:12px; align-items:flex-end; flex:1 }}
.prod h4 {{ font-size:1rem; color:var(--grafite); font-weight:700; line-height:1.3; margin-top:6px }}
.prod .seta {{ font-size:1.2rem; color:var(--azul); transition:transform .2s }}
.prod:hover .seta {{ transform:translateX(4px) }}
.esconde {{ display:none }}

/* processo */
.passos {{ display:grid; grid-template-columns:repeat(3,1fr); gap:0; border-top:1px solid var(--grafite) }}
.passo {{ padding:34px 34px 0 0 }}
.passo .n {{ font-family:'IBM Plex Mono',monospace; font-size:.85rem; color:var(--azul) }}
.passo h3 {{ font-size:1.5rem; margin:14px 0 10px }}

/* sobre */
.sobre {{ display:grid; grid-template-columns:1fr 1fr; gap:80px; align-items:center }}
.sobre img {{ aspect-ratio:4/5; object-fit:cover; width:100% }}
.sobre p {{ margin-top:18px }}
.lista {{ display:grid; grid-template-columns:1fr 1fr; gap:14px 30px; margin-top:34px; padding-top:28px; border-top:1px solid var(--linha) }}
.lista div {{ font-weight:700; color:var(--grafite); padding-left:18px; position:relative }}
.lista div::before {{ content:''; position:absolute; left:0; top:.6em; width:8px; height:8px; background:var(--verde) }}

/* contato */
.contato {{ background:var(--grafite); color:#C9CDD2; border:none }}
.contato h2 {{ color:#fff }}
.contato .mono {{ color:#8D939A }}
.ct {{ display:grid; grid-template-columns:1.2fr 1fr; gap:80px }}
.ct dl {{ display:grid; grid-template-columns:140px 1fr; gap:22px 20px; border-top:1px solid #3A3F45; padding-top:30px }}
.ct dt {{ font-family:'IBM Plex Mono',monospace; font-size:.78rem; text-transform:uppercase; letter-spacing:.06em; color:#8D939A; padding-top:3px }}
.ct dd {{ color:#fff; font-weight:600 }}
.ct .acoes {{ display:flex; gap:14px; flex-wrap:wrap; margin-top:34px }}
.contato .btn-linha {{ border-color:#fff; color:#fff }} .contato .btn-linha:hover {{ background:#fff; color:var(--grafite) }}
footer {{ background:var(--grafite); color:#8D939A; border-top:1px solid #3A3F45; padding:28px 0; font-size:.85rem }}
footer .wrap {{ display:flex; justify-content:space-between; gap:20px; flex-wrap:wrap }}
.wa-fixo {{ position:fixed; right:22px; bottom:22px; width:58px; height:58px; border-radius:50%; background:var(--verde); display:grid; place-items:center; box-shadow:0 8px 24px rgba(0,0,0,.18); z-index:60 }}
.wa-fixo svg {{ width:30px; height:30px; fill:#fff }}

/* responsivo */
@media (max-width:1020px) {{
  .hero {{ grid-template-columns:1fr }} .hero-txt {{ padding:56px 28px }} .hero-img {{ height:min(62vh, 560px) }}
  .linhas {{ grid-template-columns:repeat(2,1fr) }} .grade {{ grid-template-columns:repeat(3,1fr) }}
  .sec-head, .sobre, .ct {{ grid-template-columns:1fr; gap:28px }} .sec-head p {{ justify-self:start }}
  .amb {{ grid-template-columns:1fr 1fr }} .amb figure:first-child {{ grid-column:1 / -1 }}
}}
@media (max-width:640px) {{
  .wrap {{ padding:0 18px }} section {{ padding:80px 0 }}
  .nav nav a:not(.btn) {{ display:none }} .nav img {{ height:42px }}
  .fatos {{ grid-template-columns:1fr 1fr }} .grade {{ grid-template-columns:1fr 1fr }}
    .linhas {{ grid-template-columns:1fr }} .linha {{ display:grid; grid-template-columns:112px 1fr; align-items:center }}
  .linha-img {{ aspect-ratio:1 }} .linha-txt {{ padding:14px 16px }} .linha p {{ display:none }} .linha h3 {{ margin:4px 0 0 }}
  .passos {{ grid-template-columns:1fr }} .antes {{ grid-template-columns:1fr }}
  .amb {{ grid-template-columns:1fr }} .amb figure:nth-child(3) {{ display:none }} .lista {{ grid-template-columns:1fr }} .ct dl {{ grid-template-columns:1fr; gap:4px }}
  .ct dd {{ margin-bottom:16px }} .prod .tx {{ padding:14px }}
}}
</style>
</head>
<body>

<header><div class="wrap nav">
  <a href="#topo"><img src="img/logo.png" alt="Alfa Soluções em Concreto"></a>
  <nav><a href="#linhas">Linhas</a><a href="#catalogo">Catálogo</a><a href="#como-pedir">Como pedir</a><a href="#sobre">Sobre</a>
    <a class="btn btn-azul" href="{WA}" target="_blank" rel="noopener">Pedir orçamento</a></nav>
</div></header>

<main id="topo">
<div class="hero">
  <div class="hero-txt">
    <span class="mono">Pré-moldados de concreto · Araçatuba-SP</span>
    <h1>Solidez, design e resistência <em>em concreto.</em></h1>
    <p class="lead">Revestimentos 3D, cobogós, mesas, bancos e peças de acabamento produzidos em fábrica própria, com peças sob medida para o seu projeto.</p>
    <div class="acoes">
      <a class="btn btn-azul" href="#catalogo">Ver catálogo →</a>
      <a class="btn btn-linha" href="{WA}" target="_blank" rel="noopener">Falar no WhatsApp</a>
    </div>
    <div class="fatos">
      <div><b>{len(prods)}</b><span class="mono">produtos</span></div>
      <div><b>5</b><span class="mono">linhas</span></div>
      <div><b>Sob medida</b><span class="mono">projetos especiais</span></div>
      <div><b>Entrega</b><span class="mono">na região</span></div>
    </div>
  </div>
  <figure class="hero-img"><img src="img/floral-sala.jpg" alt="Sala com parede em revestimento 3D de concreto Floral"><figcaption class="mono">Revestimento Floral · ambiente ilustrativo</figcaption></figure>
</div>

<section id="linhas"><div class="wrap">
  <div class="sec-head"><div><span class="mono">Linhas de produtos</span><h2>Cinco linhas para a obra inteira.</h2></div>
    <p>Do jardim à fachada: escolha a linha e veja todos os modelos disponíveis no catálogo.</p></div>
  <div class="linhas">
{linhas}
  </div>
</div></section>

<section id="ambientes"><div class="wrap">
  <div class="sec-head"><div><span class="mono">Aplicações</span><h2>A mesma parede, outro projeto.</h2></div>
    <p>O revestimento em concreto cria relevo, sombra e textura, e a luz faz o resto ao longo do dia.</p></div>
  <div class="amb">
    <figure><img src="img/mosaico-varanda.jpg" alt="Varanda gourmet com revestimento Mosaico" loading="lazy"><figcaption><b>Mosaico</b><span class="mono">Varanda gourmet</span></figcaption></figure>
    <figure><img src="img/escaleno-entrada.jpg" alt="Hall de entrada com revestimento Escaleno" loading="lazy"><figcaption><b>Escaleno</b><span class="mono">Hall de entrada</span></figcaption></figure>
    <figure><img src="img/floral-sala.jpg" alt="Sala com revestimento Floral" loading="lazy"><figcaption><b>Floral</b><span class="mono">Sala de estar</span></figcaption></figure>
  </div>
  <div class="antes">
    <figure><span class="mono">Antes</span><img src="img/sala-lisa.jpg" alt="Sala com parede lisa" loading="lazy"></figure>
    <figure><span class="mono">Depois · Floral</span><img src="img/floral-sala.jpg" alt="A mesma sala com revestimento Floral" loading="lazy"></figure>
  </div>
  <p class="mono nota">Ambientes ilustrativos com produtos do catálogo.</p>
</div></section>

<span id="produtos"></span><section id="catalogo"><div class="wrap">
  <div class="sec-head"><div><span class="mono">Catálogo</span><h2>{len(prods)} produtos em concreto.</h2></div>
    <p>Filtre por linha e clique no produto para ver medidas e características.</p></div>
  <div class="abas">
{abas}
  </div>
  <div class="grade" id="grade"></div>
</div></section>

<section id="como-pedir"><div class="wrap">
  <div class="sec-head"><div><span class="mono">Como pedir</span><h2>Do modelo ao orçamento em três passos.</h2></div>
    <p>Atendemos arquitetos, engenheiros, construtoras e clientes diretos.</p></div>
  <div class="passos">
    <div class="passo"><span class="n">01</span><h3>Escolha o modelo</h3><p>Navegue pelo catálogo e separe as peças que combinam com o seu projeto.</p></div>
    <div class="passo"><span class="n">02</span><h3>Envie as medidas</h3><p>Mande pelo WhatsApp a metragem ou a quantidade. Peças sob medida também são possíveis.</p></div>
    <div class="passo"><span class="n">03</span><h3>Receba o orçamento</h3><p>Orçamento sem compromisso, com entrega na região de Araçatuba.</p></div>
  </div>
</div></section>

<section id="sobre"><div class="wrap sobre">
  <img src="img/escaleno-entrada.jpg" alt="Revestimento em concreto Escaleno" loading="lazy">
  <div>
    <span class="mono">Sobre a Alfa</span>
    <h2>Tradição e qualidade em concreto pré-moldado.</h2>
    <p>A Alfa Soluções em Concreto fabrica produtos pré-moldados para construção civil, paisagismo e projetos arquitetônicos.</p>
    <p>Em Araçatuba-SP, nossa estrutura produtiva e o controle de qualidade garantem peças que unem resistência, estética e funcionalidade, com atendimento próximo do início ao fim.</p>
    <div class="lista"><div>Concreto premium</div><div>Alta resistência</div><div>Peças sob medida</div><div>Entrega na região</div></div>
  </div>
</div></section>

<section class="contato" id="contato"><div class="wrap ct">
  <div>
    <span class="mono">Contato</span>
    <h2>Vamos tirar o seu projeto do papel?</h2>
    <div class="acoes">
      <a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">Pedir orçamento no WhatsApp</a>
      <a class="btn btn-linha" href="https://www.google.com/maps/search/?api=1&query=R.+Ant%C3%B4nio+Afonso+de+Toledo,+369,+Ara%C3%A7atuba" target="_blank" rel="noopener">Como chegar</a>
    </div>
  </div>
  <dl>
    <dt>Endereço</dt><dd>R. Antônio Afonso de Toledo, 369<br>Jardim Sumaré, Araçatuba-SP</dd>
    <dt>Telefones</dt><dd>(18) 99760-3980<br>(18) 99676-9650</dd>
    <dt>Horário</dt><dd>Seg. a sex., 7h às 17h<br>Sábados a consultar</dd>
  </dl>
</div></section>
</main>

<footer><div class="wrap"><span>© 2026 Alfa Soluções em Concreto · Araçatuba-SP</span><span>Concreto pré-moldado para construção, paisagismo e arquitetura</span></div></footer>

<a class="wa-fixo" href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp"><svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.4-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.2c0-.1-.2-.2-.4-.3z"/></svg></a>

<script>
const CAT = {json.dumps(CAT, ensure_ascii=False)};
const P = {json.dumps(prods, ensure_ascii=False)};
const g = document.getElementById('grade');
g.innerHTML = P.map(p => `<a class="prod" data-cat="${{p.c}}" href="produto.html?id=${{p.id}}">
  <div class="ft"><img src="${{p.i}}" alt="${{p.n}}" loading="lazy"></div>
  <div class="tx"><div><span class="mono">${{CAT[p.c]}}</span><h4>${{p.n}}</h4></div><span class="seta">→</span></div></a>`).join('');
function filtra(c) {{
  document.querySelectorAll('.aba').forEach(b => b.classList.toggle('ativa', b.dataset.cat === c));
  document.querySelectorAll('.prod').forEach(el => el.classList.toggle('esconde', c !== 'todos' && el.dataset.cat !== c));
}}
document.querySelectorAll('.aba').forEach(b => b.addEventListener('click', () => filtra(b.dataset.cat)));
document.querySelectorAll('[data-filtro]').forEach(a => a.addEventListener('click', () => filtra(a.dataset.filtro)));
</script>
</body>
</html>
'''
open('index.html', 'w', encoding='utf-8').write(pagina)
print('ok', len(prods), cont)
