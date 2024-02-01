#!/usr/bin/python3
import subprocess
import json

def check_dns_service_and_zone_transfer_status():
    results = {
        "분류": "시스템 관리",
        "코드": "U-34",
        "위험도": "상",
        "진단 항목": "DNS Zone Transfer 설정",
        "진단 결과": "",
        "현황": [],
        "대응방안": "[양호]: DNS 서비스 미사용 또는, Zone Transfer를 허가된 사용자에게만 허용한 경우\n[취약]: DNS 서비스를 사용하여 Zone Transfer를 모든 사용자에게 허용한 경우"
    }

    # `named` 프로세스가 실행 중인지 확인
    try:
        process_output = subprocess.check_output(["ps", "-ef"], text=True)
        if "named" in process_output and not "grep named" in process_output:
            results["진단 결과"] = "취약"
            results["현황"].append("DNS 서비스 데몬이 실행 중입니다.")
        else:
            results["진단 결과"] = "양호"
            results["현황"].append("DNS 서비스 데몬이 실행되고 있지 않습니다.")
    except subprocess.CalledProcessError:
        results["현황"].append("DNS 서비스 상태 확인 중 오류 발생")
    except Exception as e:
        results["현황"].append(f"예외 발생: {str(e)}")

    return results

def main():
    results = check_dns_service_and_zone_transfer_status()
    print(json.dumps(results, ensure_ascii=False, indent=4))

if __name__ == "__main__":
    main()
