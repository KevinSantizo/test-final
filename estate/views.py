from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from estate.models import Land, Plot, Tree
from user.models import User
# Create your views here.


def index(request, user_pk):
    template = 'estate/index.html'
    context = {
        'lands': Land.objects.all(),
        'plots': Plot.objects.all(),
        'user': User.objects.get(pk=user_pk),
        'trees': Tree.objects.all(),
    }
    return render(request, template, context)


def actions(request, user_pk):
    template = 'estate/actions.html'
    context = {
        'lands': Land.objects.all(),
        'user_pk': user_pk,
        'num_lands': Land.objects.count(),
    }
    return render(request, template, context)


def new_land(request, user_pk):
    if request.method == 'POST':
        new_land = Land(
            name=request.POST['name'],
            country=request.POST['country'],
            region=request.POST['region'],
        )
        new_land.save()
        return HttpResponseRedirect(reverse('estate:actions', kwargs={'user_pk': user_pk}))
    elif request.method == 'GET':
        template = 'estate/new_land.html'
        return render(request, template, {'user_pk': user_pk})
    return HttpResponseRedirect('No se Puede guardar!')


def edit_land(request, land_pk):
    if request.method == 'POST':
        updated_land = Land.objects.get(pk=land_pk)
        updated_land.name = request.POST['name']
        updated_land.country = request.POST['country']
        updated_land.region = request.POST['region']
        updated_land.save()

        return HttpResponseRedirect(reverse('estate:actions', kwargs={'user_pk': land_pk}))
    elif request.method == 'GET':
        temlate = 'estate/edit_land.html'
        context = {
            'land': Land.objects.get(pk=land_pk),
            'user_pk': land_pk,
        }
        return render(request, temlate, context)
    return HttpResponse('No se puede atualizar')


def delete_land(request, land_pk):
    deleted_land = Land.objects.get(pk=land_pk)
    deleted_land.delete()

    return HttpResponseRedirect(reverse('estate:actions', kwargs={'user_pk': land_pk}))


def actions_plot(request, user_pk):
    template = 'estate/actions_plot.html'
    context = {
        'plots': Plot.objects.all(),
        'user_pk': user_pk,
        'num_plots': Plot.objects.count(),
    }
    return render(request, template, context)


def new_plot(request, user_pk):
    if request.method == 'POST':
        post_land = Land.objects.get(pk=request.POST['land'])
        new_plot = Plot(
            land=post_land,
            name=request.POST['name'],
            latitude=request.POST['latitude'],
            length=request.POST['length'],
        )
        new_plot.save()

        return HttpResponseRedirect(reverse('estate:actions-plot', kwargs={'user_pk': user_pk}))
    elif request.method == 'GET':
        template = 'estate/new_plot.html'
        context = {
            'lands': Land.objects.all(),
            'user_pk': user_pk,
        }
        return render(request, template, context)
    return HttpResponse('No se puede guardar!!!')


def edit_plot(request, plot_pk):
    if request.method == 'POST':
        post_land = Land.objects.get(pk=request.POST['land'])
        updated_plot = Plot.objects.get(pk=plot_pk)
        updated_plot.land = post_land
        updated_plot.name = request.POST['name']
        updated_plot.latitude = request.POST['latitude']
        updated_plot.length = request.POST['length']
        updated_plot.save()

        return HttpResponseRedirect(reverse('estate:actions-plot', kwargs={'user_pk': plot_pk}))
    elif request.method == 'GET':
        template = 'estate/edit_plot.html'
        land_plot = Plot.objects.get(pk=plot_pk)
        context = {
            'plot': Plot.objects.get(pk=plot_pk),
            'lands': Land.objects.all(),
            'land_instance': land_plot,
            'plot_pk': plot_pk,
        }
        return render(request, template, context)
    return HttpResponse('No se puede guardar')


def delete_plot(request, plot_pk):
    delete_plot = Plot.objects.get(pk=plot_pk)
    delete_plot.delete()

    return HttpResponseRedirect(reverse('estate:actions-plot', kwargs={'user_pk': plot_pk}))


def actions_tree_admin(request, user_pk):
    template = 'estate/actions_tree_admin.html'
    context = {
        'trees': Tree.objects.all(),
        'user_pk': user_pk,
        'num_trees': Tree.objects.count(),
    }
    return render(request, template, context)


def actions_tree_user(request, user_pk):
    template = 'estate/actions_tree_user.html'
    context = {
        'trees': Tree.objects.all(),
        'user_pk': user_pk,
        'num_trees': Tree.objects.count(),
    }
    return render(request, template, context)


def new_tree(request, user_pk):
    if request.method == 'POST':
        post_plot = Plot.objects.get(pk=request.POST['plot'])
        new_tree= Tree(
            plot=post_plot,
            diameter=request.POST['diameter'],
            height=request.POST['height'],
            health=request.POST['health'],
            year=request.POST['year'],
        )
        new_tree.save()

        return HttpResponseRedirect(reverse('estate:index', kwargs={'user_pk': user_pk}))
    elif request.method == 'GET':
        template = 'estate/new_tree.html'
        context = {
            'user_pk': user_pk,
            'plots': Plot.objects.all(),
        }
        return render(request, template, context)
    return HttpResponse('No se puede guardar')


def edit_tree(request, tree_pk):
        if request.method == 'POST':
            post_plot = Plot.objects.get(pk=request.POST['plot'])
            update_tree = Tree.objects.get(pk=tree_pk)
            update_tree.plot = post_plot
            update_tree.diameter = request.POST['diameter']
            update_tree.height = request.POST['height']
            update_tree.health = request.POST['health']
            update_tree.year = request.POST['year']
            update_tree.save()

            return HttpResponseRedirect(reverse('estate:actions-tree-admin', kwargs={'user_pk': tree_pk}))
        elif request.method == 'GET':
            template = 'estate/edit_tree.html'
            plot_tree = Tree.objects.get(pk=tree_pk)
            context = {
                'tree': Tree.objects.get(pk=tree_pk),
                'plots': Plot.objects.all(),
                'plot_instance': plot_tree,
                'tree_pk': tree_pk,
            }
            return render(request, template, context)
        return HttpResponse('No se Puede Guardar')


def delete_tree(request, tree_pk):
    delete_tree = Tree.objects.get(pk=tree_pk)
    delete_tree.delete()

    return HttpResponseRedirect(reverse('estate:actions-tree-admin', kwargs={'user_pk': tree_pk}))


