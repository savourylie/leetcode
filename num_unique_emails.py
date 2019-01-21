class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result_set = set()

        for email in emails:
            local_name, domain_name = self._parse_email(email)

            index = self._plus_index(local_name)

            if index is not None:
                local_name = local_name[:index]

            local_name = self._original_name(local_name)

            if (local_name, domain_name) not in result_set:
                result_set.add((local_name, domain_name))

        return len(result_set)

    def _parse_email(self, email):
        local_name, domain_name = email.split('@')

        return local_name, domain_name

    def _plus_index(self, local_name):
        for i, x in enumerate(local_name):
            if x == '+':
                return i

        return None

    def _original_name(self, local_name):
        result_name = ''

        for x in local_name:
            if x != '.':
                result_name += x

        return result_name

if __name__ == '__main__':
    emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com",
              "testemail+david@lee.tcode.com"]

    s = Solution()
    assert s.numUniqueEmails(emails) == 2