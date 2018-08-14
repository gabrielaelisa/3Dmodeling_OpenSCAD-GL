$fn= 50;
//sphere(r=3);
module hand(){
    cylinder(r=2,h=0.5, center=true);
    
    module palm(){
        difference(){
            translate([0 ,0 , -1.5])
            sphere(r=2.5);
            translate([0 ,0 , -2.5])
            cylinder(r=2.5,h=5,     center=true);
        }
    }
  
    palm();
    //cylinder(r=0.2,h=10, center=true);
    
}

//hand();
module hand2(){
   module fingers(){
    $fn= 10;
    rotate(a=-25, v=[1,0,0])
    rotate(a=20, v=[0,1,0])
    translate([2.8 ,0,1.3])
    sphere(r=0.4);
       
    rotate(a=-10, v=[1,0,0])
    rotate(a=20, v=[0,1,0])
    translate([2.8 ,0,0])
    cube([0.4, 0.3, 2], center=true);
    
    rotate(a=-25, v=[1,0,0])
    rotate(a=-10, v=[0,1,0])
    translate([0 ,-0.2,1.2])
    sphere(r=0.5);
       
    rotate(a=-10, v=[1,0,0])
    rotate(a=-10, v=[0,1,0])
    cube([0.4, 0.4, 2.5], center=true);
    
    rotate(a=-10, v=[1,0,0])
    rotate(a=15, v=[0,1,0])
    translate([2 ,-0.2,1.4])
    sphere(r=0.5);
    
    rotate(a=-10, v=[1,0,0])
    rotate(a=15, v=[0,1,0])
    translate([2 ,0,0.2])
    cube([0.4, 0.4, 2.5], center=true);
    
    rotate(a=-15, v=[1,0,0])
    rotate(a=10, v=[0,1,0])
    translate([1 ,-0.2,1.3])
    sphere(r=0.5);
    
    rotate(a=-10, v=[1,0,0])
    rotate(a=10, v=[0,1,0])
    translate([1 ,0,0.2])
    cube([0.38, 0.5, 2.5], center=true);
    
    rotate(a=-5, v=[1,0,0])
    rotate(a=-70, v=[0,1,0])
    translate([-1.8 ,0,0.9])
    sphere(r=0.5);
    
    rotate(a=-5, v=[1,0,0])
    translate([-0.5 ,0,1.5])
    rotate(a=-70, v=[0,1,0])
    translate([-3 ,0,-1])
    cube([0.4, 0.3, 2], center=true);
}
   module palm(){
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
translate([0.2,0,1.8])
fingers();
palm();
translate([1.4,-1.3, -1.62])

rotate(a=100, v=[1,0,0])
cylinder(2,1.3,0.4, center=true, $fn=100);
}
//hand();

hand2();
