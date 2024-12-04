# Analysis-of-Satellite-Supply-Chain-and-Communication-Security-Vulnerabilities-Using-NOS3

Topic: 우주 산업의 민간화와 인공위성의 증가로 우주 보안의 중요성이 커지고 있다. 본 연구에서는 NASA의 NOS3 시뮬레이터를 활용해 악성 코드 삽입 및 공격 시나리오를 구현하여 위성 공급망과 위성 통신에 대한 보안 강화의 필요성을 보였다.

## Main File Description

### 위성 비행 소프트웨어 관련
- `generic_reaction_wheel_app.c` : 반작용휠(Reaction Wheel)의 기능과 관련된 fsw(flight software) 파일. 해당 파일에 위성의 fsw를 무한히 종료시키는 악성코드를 삽입함. (아래 캡쳐 참고)

![스크린샷 2024-11-29 153405](https://github.com/user-attachments/assets/b00a8ef4-03a9-4a75-829e-6103735be66f)

- `generic_rw_hardware_model.cpp` : 반작용휠의 가상 하드웨어 모델 파일. 해당 파일로 반작용휠이 NOS Engine에서 구현한 가상 UART 통신을 함을 알 수 있음.
- `hwlib.h` : UART 통신과 더불어 GPIO, I2C, CAN 과 같은 다양한 통신 프로토콜이 가상으로 구현된 파일. 

### 위성 제어를 위한 지상국의 CMD
- `GENERIC_REACTION_WHEEL_CMD.txt` : COSMOS 지상국에서 보낼 수 있는 반작용휠과 관련된 CMD가 정의된 파일. CCSDS Space Protocol의 해더 포멧을 따름. (아래 캡쳐 참고)

![스크린샷 2024-11-29 150303](https://github.com/user-attachments/assets/c7bfd72c-cd57-47da-9246-080895307ed3)


### 비인가 신호 송신 스크립트
- `malicious_ccsds.py` : COSMOS 지상국을 사용하지 않고 비인가 신호를 송신하기 위해 작성한 파이썬 스크립트. 성공적으로 신호를 송신하기 위해서는 가동 중의 fsw 컨테이너의 IP 주소와 Port를 알아야 함. 
