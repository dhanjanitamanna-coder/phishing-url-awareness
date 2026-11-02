import ipaddress
from urllib.parse import urlsplit


def check_url(url):
    warnings = []

    try:
        parsed = urlsplit(url)
        hostname = parsed.hostname

        if not parsed.scheme or not hostname:
            print("Invalid URL. Please enter a complete URL.") 
            return

        # 1. Check @ symbol
        if "@" in url:
            warnings.append("URL contains an @ symbol.")

        # 2. Check URL length
        if len(url) > 100:
            warnings.append("URL is longer than 100 characters.")

        # 3. Check IP address hostname
        try:
            ipaddress.ip_address(hostname)
            warnings.append("URL uses an IP address instead of a domain name.")
        except ValueError:
            pass

        # 4. Check hostname segments
        if len(hostname.split(".")) >= 5:
            warnings.append("Hostname contains 5 or more segments.")

        # 5. Check punycode
        if "xn--" in hostname.lower():
            warnings.append("Hostname contains a punycode marker (xn--).")

        # 6. Check HTTP
        if parsed.scheme.lower() == "http":
            warnings.append("URL uses HTTP instead of HTTPS.")

        print("\n--- URL CHECK RESULT ---")

        if warnings:
            print("Warning signs found:")
            for warning in warnings:
                print("- " + warning)

            print("\nResult: Review this URL carefully.")
        else:
            print("No listed warning signs found.")
            print("This does NOT guarantee that the URL is safe.")

    except ValueError:
        print("Invalid URL format. Please enter a valid URL.")


def main():
    print("====================================")
    print("     PHISHING URL AWARENESS CHECKER")
    print("====================================")

    while True:
        url = input("\nEnter URL (or type 'quit' to exit): ").strip()

        if url.lower() == "quit":
            print("Thank you for using the checker!")
            break

        if not url:
            print("Please enter a URL.")
            continue

        check_url(url)


if __name__ == "__main__":
    main()