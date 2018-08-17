$fn= 50;


module hand2(){
   module fingers(){
    $fn= 10;
    rotate(a=-25, v=[1,0,0])
    rotate(a=20, v=[0,1,0])
    translate([2.8 ,0,1.3])
    color([1,0,0])
    sphere(r=0.4);
    
    color([1,1,1])
    rotate(a=-10, v=[1,0,0])
    rotate(a=20, v=[0,1,0])
    translate([2.8 ,0,0])
    cube([0.4, 0.3, 2], center=true);
    
    rotate(a=-25, v=[1,0,0])
    rotate(a=-10, v=[0,1,0])
    translate([0 ,-0.2,1.2])
    color([1,0,0])
    sphere(r=0.5);
       
    rotate(a=-10, v=[1,0,0])
    rotate(a=-10, v=[0,1,0])
    color([1,1,1])
    cube([0.4, 0.4, 2.5], center=true);
    
    rotate(a=-10, v=[1,0,0])
    rotate(a=15, v=[0,1,0])
    translate([2 ,-0.2,1.4])
    color([1,0,0])
    sphere(r=0.5);
    
    rotate(a=-10, v=[1,0,0])
    rotate(a=15, v=[0,1,0])
    translate([2 ,0,0.2])
    color([1,1,1])
    cube([0.4, 0.4, 2.5], center=true);
    
    rotate(a=-15, v=[1,0,0])
    rotate(a=10, v=[0,1,0])
    translate([1 ,-0.2,1.3])
    color([1,0,0])
    sphere(r=0.5);
    
    rotate(a=-10, v=[1,0,0])
    rotate(a=10, v=[0,1,0])
    translate([1 ,0,0.2])
    color([1,1,1])
    cube([0.38, 0.5, 2.5], center=true);
    
    rotate(a=-5, v=[1,0,0])
    rotate(a=-70, v=[0,1,0])
    translate([-1.8 ,0,0.9])
    color([1,0,0])
    sphere(r=0.5);
    
    rotate(a=-5, v=[1,0,0])
    translate([-0.5 ,0,1.5])
    rotate(a=-70, v=[0,1,0])
    translate([-3 ,0,-1])
    color([1,1,1])
    cube([0.4, 0.3, 2], center=true);
}
module palm(){
   color([1,1,1])
   rotate(a=180, v=[1,0,0])
   intersection(){
       translate([0, 0, -3])
       cube([2.8, 0.5, 10]);
       union() 
       {
           cube([2.8, 0.5, 1.5]);
           translate([1.4, 0, 0])
           sphere(r=1.5);
           translate([1.4, 0, 1.2])
           sphere(r=1.5);
       }
   }
    
}
    module handaux(){
        translate([0.2,0,1.8])
        fingers();
        palm();
        translate([1.4,-1.3, -1.62])

        rotate(a=100, v=[1,0,0])
        //cone circle base
        color([1,1,1])
        cylinder(2,1.3,0.4, center=true, $fn=100);
    }
    rotate(a=20, v=[1, 0, 0])
    handaux();
    translate([1.4, -5.6, -4.8])
    rotate(a=120, v=[1,0,0])
    color([1,0.6,0.4])
    cylinder(r= 0.5, h= 10 ,center=true);
    translate([1.4,-13, -4.7])
    rotate(a=42, v=[1,0,0])
    color([1,0.6,0.4])
    cylinder(r= 0.5, h= 7,center=true);
    translate([1.4,-10.3, -7.5 ])
    color([1,0.6,0.4])
    sphere(r=0.7);
    translate([1.4,-16, - 1])
    color([1,0,0])
    sphere(r=2.5);
}
//hand();

 module prism(l, w, h){
     color([0,0,0.6])
       polyhedron(
               points=[[0,0,0], [l,0,0], [l,w,0], [0,w,0], [0,w,h], [l,w,h]],
               faces=[[0,1,2,3],[5,4,3,2],[0,4,5,1],[0,3,4],[5,2,1]]
               );}


module ear(){
    translate([5, 3, 0.5]) 
    rotate(a=90, v=[0, 0, 1])
    rotate(a=180, v=[0, 1, 0])
    prism(3, 5, 3);
    rotate(a=90, v=[0, 0, 1])
    rotate(a=90, v=[1, 0, 0])
    prism(3, 2.5, 8);
    translate([0, 0, -4.5]) 
    rotate(a=90, v=[0, 0, 1])
    rotate(a=90, v=[1, 0, 0])
    prism(3, 2.5, 3);
    translate([0, 0, -5.5])
    color([0,0,0.6])
    cube([1,3,2]);
    translate([-1, 0, -4.5])
    color([0,0,0.6])
    cube([2,3,7]);
}

module head(){
    for (a =[0.1:0.05:2])
    translate([0,0,a])
    color([1,0.6,0.4])
    sphere(r=5 -(a/3));
    translate([3,2,0])
    color([1, 0, 0])
    sphere(r=2);
    rotate(a=180, v= [0 ,1,0])
    translate([3,2,0])
    color([1, 0, 0])
    sphere(r=2);
    
    module earaux(){
        rotate(a=-20, v= [0, 0, 1])
        translate([6,-1,7])
        rotate(a= 50, v= [0, 1, 0])
        scale([0.9,0.9,0.9])
        ear();
        }
    earaux();
    mirror([1 , 0, 0])
    earaux();
}

module body()
{
   module body1(){
    for (a =[0.1:0.05:3.5])    
     translate([0,0,a])
     color([1,1,1])
     sphere(r=6.3);
    }
    module body_aux(){
        for ( a =[0.1:0.005:2])
        translate([a,0,0])
        body1();
            
            
    }
    body_aux();
    
}

module shoe(){
    color([0,0,0.6])
    translate([0, 5, 0])
    cube([3,7 ,2]);
    prism(3, 5, 2);
    translate([0, 2, -3])
    rotate(a=90, v= [1, 0, 0])
    prism(3, 3, 2);
    translate([3 ,4, -3])
    rotate(a=180, v= [0, 0, 1])
    prism(3, 2, 1);
    translate([0,10.5,-0.7])
    color([0,0,0.6])
    cube([3,2 ,2.7]);
 
    //leg
    
    translate([0, 13, -13])
    color([1,0,0])
    sphere(r=2.5);
    translate([1, 13, -12])
    rotate(a = 50, v= [1, 0, 0])
    color([1,0.6,0.4])
    cylinder(r=1, h=8);
    translate([1, 6, -6])
    rotate(a = -40, v= [1, 0, 0])
    color([1,0.6,0.4])
    cylinder(r=1, h=8);
    
    translate([1, 6, -6.5])
    color([1, 1, 1])
    sphere(r=1.5);
}

module leg(){
    translate([7, -12 ,-23])
    rotate(a=-50, v=[0, 0, 1])
    rotate(a=180, v=[1, 0, 0])
    scale([0.8,0.8, 0.8])
    shoe();
}

module figure(){
    //body
    translate([-5, -18 ,-7])
    body();
    //head
    translate([-5, -17 ,5])
    head();
    //hands
    scale([1.2, 1.2, 1.2])
    hand2();
    translate([-10,0, 0])
    mirror([1, 0, 0])
    scale([1.2, 1.2, 1.2])
    hand2();
    //legs
    leg();
    translate([-10, 0, 0])
    mirror([1,0 ,0])
    leg();
} 
scale([1, 1 , 0.85])
figure();