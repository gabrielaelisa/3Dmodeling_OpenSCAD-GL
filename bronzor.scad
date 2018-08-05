$fn=50;
rotate(a=90, v=[1,0,0]) body();
 color([21/255,28/255,80/255])body_spheres();
 
color([70/255,130/255,280/255])
translate([0,-2,0])
sphere(r=4);
eyes();
face();
perimeter();
module body(){
    color([70/255,130/255,280/255])
    cylinder(r=20,h=5, center=true);
    color([21/255,28/255,80/255])cylinder(r=15,h=7,center=true);
}

module single_body_spheres(){
translate([0,0,19])sphere(r=4);
translate([0,0,-19])sphere(r=4);
    }
module body_spheres(){
    single_body_spheres();
    rotate(a=60, v=[0,1,0]) single_body_spheres();
    rotate(a=-60, v=[0,1,0]) single_body_spheres();
}

module ellipsoid(diameter, width, height) {
    linear_extrude(height = height, scale = [width/diameter,1]) circle(d = diameter); 
  }
  
module eye(){
  translate([9,0,0])
  rotate(a=90, v=[1,0,0])
  union(){
      color([0,0,0])
      ellipsoid(7,4,3.8);
  color([1,1,1])
  difference(){
    ellipsoid(7,4,4);
    ellipsoid(3.5,1,5);}
    }
  }
 module eyes(){
    eye();
    //rotate(a=180, v=[0,1,0])
    translate([-18,0,0])
    eye(); 
   }
module perimeter(){
    color([0,0,0])
    translate([0,-3.2,0])
    rotate(a=90, v=[1,0,0]) 
    difference(){
        circle(9.7,ceter=true);
        circle(9.5, ceter=true);
    
        }
}
module face_cylinder(){
    color([70/255,130/255,280/255])
    translate([0,-1,9.6])
    rotate(a=90, v=[1,0,0]) 
    cylinder(r=1, h=5.7, center=true);
}

module face(){
    rotate(a=30, v=[0,1,0])  
    face_cylinder();
    rotate(a=150, v=[0,1,0])  
    face_cylinder();
    rotate(a=-30, v=[0,1,0])  
    face_cylinder();
    rotate(a=-150, v=[0,1,0])  
    face_cylinder();
    
}
module leaf(w,rad,height){
    color([70/255,130/255,280/255])
hull(){
translate([(w/2)-r,0,0])cylinder(r=rad-0.45,h=height, center=true);
rotate([0,0,20])translate([(w/2)-rad-0.5,0,0])cylinder(r=rad,h=height, center=true);
rotate([0,0,20])translate([(w/2)-rad,0,0])cylinder(r=rad,h=height, center=true);
rotate([0,0,75])translate([(w/2)-rad,0,0])cylinder(r=rad,h=height, center=true);
rotate([0,0,140])translate([(w/2)-rad+1,0,0])cylinder(r=rad,h=height, center=true);

        }
}

module leafs(){
    module oneside(){
    translate([-7,3.4,0])
    rotate([90,0,0])
    leaf(7,0.5,1);
    translate([-7,3.4,-7])
    rotate([90,0,0])
    leaf(7,0.5,1);
    }
    translate([-2.43,3.4,7])
    rotate([90,75,0])
    leaf(10,0.8,1);
    oneside();
    mirror(v=[1,0,0])
    oneside();
}
module branches(){

    translate([0,3 ,-4])
    cube([1,2,14], center=true);
    module subbranch(){
        
        translate([-2,3 ,-6.8])
        rotate([0,-70,0])
        cube([1,2,5], center=true);
        translate([-2,3 ,0.2])
        rotate([0,-70,0])
        cube([1,2,5], center=true);
    }
    subbranch();
    mirror(v=[1,0,0])
    subbranch();
}
color([70/255,130/255,280/255])
branches();
leafs();

