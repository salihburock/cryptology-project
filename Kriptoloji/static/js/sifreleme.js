// window.onload = () => {
//     var auto = setTimeout(function(){ autoRefresh(); }, 100);

//     function submitform(){
//         document.forms["sifreleme"].submit();
//     }i   
//     function autoRefresh(){
//         clearTimeout(auto);
//         auto = setTimeout(function(){ submitform(); autoRefresh(); }, 10000);
//     }
// }
document.getElementById('myVideo').playbackRate= 1.5

var vidstr = `<video style="width: 1575; height: 400px; position: fixed;" id='sonucvideo' controls>
<source src="/static/ftest.mp4" type="video/mp4"/></video>
`
var keystr = `
<a style="font-size: 18px;height: %10; width: 1580; position: fixed; margin-top:400px;  "
href='/static/ftest.key' id='bilgi'>ᵺ〆ᮙ剤⿏⿖⾽剉⇲ᾌ↵刿ᮣ刭⿴剜〉剞⤥⿪别⿙ᶖ⾻⿯ᾄ⿴ᾂ刣⿡刳─⿫刯Ⓠ⿠⿐、⾹⇂剒⇟┈削⿑ⓐ⾽⤺⾵⿭剟⾿᭱⿖⤜⿯⿱刧⿰⿔Ὃ↥⿈↲ᶐ⿉ᮐ刣⿥⿌⿗剛↱ᾏ⇕剣᮲剚⿆刲⿆剀⤢⾼剢⾴ᶇ⿘⾺ὠ⾳Ὕ别⾽剢⓱⾴刚Ⓝ、⿥⾶⿑⇜剎⇰⓷剚⾼⓪⿾⤔　⿺剂⿏᭷⿹⤧⿢⿂刳⾺⿠ᾚ↬⿇⇋]
𓸗
<span class="ahovert">Anahtar dosyasını yüklemek için tıklayın.</span>
</a>
`
e = document.getElementById('buton')
function showRes(elm, elm2, pht) {
    elm.innerHTML = vidstr
    elm2.innerHTML = keystr
    pht.innerHTML = ""
}
var k = new Array("Encrypting.","Encrypting..","Encrypting...")
var pht = document.getElementById('plhot')
function changepht(i)
 {
    e['value'] = k[i]
 }
function handleSubmit() {
    elm = document.getElementById('sonucvideo')
    elm2 = document.getElementById('bilgi')
    for (let i=0;i<9;i++) {
        setTimeout(() => changepht(i%3), i*602);
    }
    setTimeout(() => showRes(elm, elm2, pht), 5423)
    
}