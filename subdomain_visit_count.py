from collections import Counter

class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        counter_list = []
        
        for x in cpdomains:
            n_str, domain = x.split(' ')
            dot_idx = [i for i, y in enumerate(domain) if y == '.']
            domains = [domain]
            for idx in dot_idx:
                domains += [domain[idx + 1:]]
                
            domain_counter = Counter()
            
            for dom in domains:
                domain_counter[dom] = int(n_str)
                
            counter_list.append(domain_counter)
            
        counter_sum = sum(counter_list, Counter())
        
        return [str(count) + ' ' + dom for dom, count in counter_sum.items()]