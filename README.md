# MY-OSS
개인과제 저장소
package ch07;

public class car {
	String model;
	int speed;
	
	car(String model) {
		this.model = model; 
	}
	void setSpeed(int speed) {
		this.speed = speed;
	}
	void run() {
		this.setSpeed(100);
		System.out.println(this.model + "가 달립니다.(시속:" + this.speed+"km/h)");
	}

}
