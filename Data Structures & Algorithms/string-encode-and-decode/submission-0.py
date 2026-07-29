class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        lens = []
        for s in strs:
            lens.append(str(len(s)))

        encoded_str = ",".join(lens) + "#"
        for s in strs:
            encoded_str += s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        i = 0
        while s[i] != "#":
            i += 1
        lens = s[:i].split(",")
        decoded_encoded = []
        
        for j in range(len(lens)):
            decoded_encoded.append(s[i+1:i+int(lens[j])+1])
            i += int(lens[j])

        return decoded_encoded
