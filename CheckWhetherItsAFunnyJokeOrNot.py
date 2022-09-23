class server:
    def writeaFunnyQuote():
        print("funnyquote:1")
        print("I'm sick of following my dreams, man. I am just going to ask where they are going and hook up with ’em later.")
        print("funnyquote:2")
        print("Before you criticize someone, you should walk a mile in their shoes. That way when you criticize them, you are a mile away from them and you have their shoes.")
        print("funnyquote:3")
        print("Before you marry a person, you should first make them use a computer with slow Internet to see who they really are.")
        print("funnyquote:4")
        print("I love being married. It's so great to find that one special person you want to annoy for the rest of your life.")
        print(end = '\n')
        print("Now its your turn to write a Funny Quote")
        for i in range(1, 6):
            writeaFunnyQuote = str(input())
            wordcount = len(writeaFunnyQuote.split())
            if wordcount <= 10:
                print("No! it's not a funny quote")
            else:
                print("Wow! it's funny")


print(server.writeaFunnyQuote())