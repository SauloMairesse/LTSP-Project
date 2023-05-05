# Computer4everyone

## 🔖&nbsp; Sobre
Diante da necessidade apresentada por diversos responsáveis técnicos por laboratórios do Campus Palmas do Instituto Federal do Tocantins, em especial da área de informática, notou-se que eles acabam desperdiçando um tempo considerável para configurar todas as máquinas de cada laboratório manualmente, tornando o trabalho desgastante e repetitivo.

Com base nisso, a ConsuTech está desenvolvendo o projeto Computer4Everyone, visando solucionar esse impedimento através do LTSP (Linux Terminal Server Project), um Projeto de Servidor de Terminais baseado em Linux, onde se utiliza uma combinação de vários serviços, permitindo que as estações não apenas executem aplicativos instalados no servidor, mas de fato ofereçam a possibilidade de iniciar computadores usando a rede, baixando todos os softwares que precisam diretamente do servidor. 

### Figura 1 - Computadores do laboratório executando através da rede
![Computadores do laboratório executando através da rede](/docs/imgs/fig1.jpg)

No que diz respeito a utilização dessa ferramenta, com a intenção de automatizar a administração das várias estações de computadores, torna-se possível que a partir de um único servidor as máquinas conectadas à rede utilizem os mais diversos softwares. Fora isso, com esse projeto, máquinas conectadas à rede que não possuam disco rígido, conseguirão executar todas suas funções normalmente, proporcionando dessa forma não apenas o gerenciamento de laboratórios das instituições de ensino, como também qualquer rede de computadores de organizações públicas ou privadas.

Além disso, o projeto também está desenvolvendo uma página web para realizar o gerenciamento do “Computer 4 Everyone”, de forma prática e eficiente para que diferentes usuários possam fazer a gestão sem a necessidade de realizar um treinamento prévio ou possuir um conhecimento específico.

### Figura 2 - Protótipo da página de gerenciamento
![Protótipo da página de gerenciamento](/docs/imgs/fig2.png)

Cada função disponível para gerência é exibida através de um card contendo uma breve explicação de seu funcionamento para minimizar o risco de equívocos ao utilizá-la e um botão que redireciona para a página da configuração solicitada. Está sendo utilizado HTML, CSS e JavaScript para o cliente e CGI (Common Gateway Interface) para que seja possível realizar a interação entre scripts de Servidores HTTP com Gateway Scripts.

## 🔖&nbsp; Instalando o servidor ltsp

Primeiro é preciso que se torne um super usuário. É possível alcançar esse estado ao rodar o seguinte comando. Será pedido a senha do seu usuário.

```bash
sudo su
```

Em seguida, execute o arquivo computer4everyone.sh no diretório em que foi baixado.

```bash
bash computer4everyone.sh
```

Se não souber  em qual diretório o arquivo está, execute o comando abaixo.

```bash
find -iname computer4everyone.sh
```

Ao executar o arquivo, irão aparecer algumas perguntas. Irá levar um tempo considerável, mas em alguns momentos será pedido informações. Por isso, não se afaste por muito tempo. Logo que terminar de criar a imagem do ltsp, deve-se configurá-lo. 

Ao rodar o comando abaixo, o arquivo default será aberto no terminal. Mude minhaimagem para o nome da imagem escolhida. Não esqueça de salvar.

```bash
pico /srv/tftp/ltsp/pxelinux.cfg/default
```

Agora vamos configurar o dnsmasq. Dentro do arquivo que será aberto, no final, terá algumas linhas parecidas com a imagem abaixo.

![Imagem do arquivo ltsp-dnsmasq.conf já configurado ](/docs/imgs/fig3.jpg)

Para abrir o arquivo:

```bash
pico  /etc/dnsmasq.d/ltsp-dnsmasq.conf
```

Acrescente as linhas sinalizadas com a seta vermelha em seu arquivo nas posições indicadas. O primeiro comando no início, e o segundo no início e no final.

```bash
pxe-service=tag:pxelinux,X86PC,"pxelinux.0",ltsp/pxelinux.0
```

```bash
dhcp-boot=tag:pxelinux,ltsp/pxelinux.0
```

Depois de salvar as alterações e fechar o arquivo, remova o arquivo resolv.conf. Será criado outro automaticamente após reiniciar o serviço.

```bash
sudo rm -rf /etc/resolv.conf
```
Retire o systemd-resolved da inicialização do sistema.
```bash
sudo systemctl disable systemd-resolved
```

Pare o serviço systemd-resolved.
```bash
sudo systemctl stop systemd-resolved
```

Reinicie o NetworkManager para gerar um novo resolv.conf e assim gerenciar a resolução DNS.

```bash
sudo systemctl restart network-manager
```
