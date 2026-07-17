from langchain_text_splitters import CharacterTextSplitter,RecursiveCharacterTextSplitter
from langchain_experimental.text_splitter import SemanticChunker

splitter = CharacterTextSplitter()

text = "cndkakv kcnckvnak c kv kdv c ikjkv kc ak fcvcvkdcncnjav mNDNDKAKDSNJKASD FKNINFKSDBKDFBKDSAVBKD D VKSBIDBK MBAIESDMNVJCHFHEIFHAkf, innkcv cIMNDS CMNSd fiNDd kKEBFIJenksd ksfbeoD,D, MHS,c ksbkjadjamnmc kaj"

print(splitter.split_text(text))

# ['cndkakv kcnckvnak c kv kdv c ikjkv kc ak fcvcvkdcncnjav mNDNDKAKDSNJKASD FKNINFKSDBKDFBKDSAVBKD D VKSBIDBK MBAIESDMNVJCHFHEIFHAkf, innkcv cIMNDS CMNSd fiNDd kKEBFIJenksd ksfbeoD,D, MHS,c ksbkjadjamnmc kaj']



splitter = RecursiveCharacterTextSplitter(
    chunk_size = 20,
    chunk_overlap = 0
)


print(splitter.split_text(text,))

#['cndkakv kcnckvnak c kv kdv c ikjkv kc ak fcvcvkdcncnjav mNDNDKAKDSNJKASD FKNINFKSDBKDFBKDSAVBKD D VKSBIDBK MBAIESDMNVJCHFHEIFHAkf, innkcv cIMNDS CMNSd fiNDd kKEBFIJenksd ksfbeoD,D, MHS,c ksbkjadjamnmc kaj']

splittter = ()