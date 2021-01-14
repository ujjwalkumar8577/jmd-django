function calculate() {

    document.getElementById("details-btn").style.visibility = "hidden";

    var form = document.getElementById("order-form");

    var name=form.elements[0].value;
    var address=form.elements[1].value;
    var contact=form.elements[2].value;

    var items=["Table Butter 22 gm","Table Butter 50 gm","Table Butter 100 gm (TUB)","Table Butter 100 gm (CAKE)","Table Butter 500 gm"];
    var rates=[203,216,362,435,213];
    var qty= new Array();
    var amt=0;

    for(let i=0; i<5; i++) {
        qty[i]=form.elements[i+4].value*1;
        amt+=qty[i]*rates[i];
    }
    
    console.log("Calculated Amount : " + amt);

    var str="";
    var sno=1;
    var total=0;
    
    for(let i=3; i<=7; i++) {

        if(qty[i-3]!=0) {

            str+="<tr>";

            str+="<td>";
            str+=sno;
            str+="</td>";

            str+="<td>";
            str+=items[i-3];
            str+="</td>";

            str+="<td>";
            str+=qty[i-3];
            str+="</td>";

            str+="<td>";
            str+=rates[i-3];
            str+="</td>";

            str+="<td>";
            str+=qty[i-3]*rates[i-3];
            str+="</td>";

            str+="</tr>"

            total=total+qty[i-3]*1;
            sno++;
        }
    }

    document.getElementById("amount").innerHTML = "Your Order Amount is Rs. " + amt;
    
    document.getElementById("tab-name").innerHTML = name;
    document.getElementById("tab-address").innerHTML = address;
    document.getElementById("tab-contact").innerHTML = contact;
    document.getElementById("tab-body").innerHTML = str;
    document.getElementById("tab-qty").innerHTML = total;
    document.getElementById("tab-amt").innerHTML = amt;
    document.getElementById("tab-amt-pb").innerHTML = amt;

    if(amt>0) {
        document.getElementById("details-btn").style.visibility = "visible";
    }
}
