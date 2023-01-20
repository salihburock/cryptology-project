window.onload = () => {
    var auto = setTimeout(function(){ autoRefresh(); }, 100);

    function submitform(){
        document.forms["sifreleme"].submit();
    }

    function autoRefresh(){
        clearTimeout(auto);
        auto = setTimeout(function(){ submitform(); autoRefresh(); }, 10000);
    }
}